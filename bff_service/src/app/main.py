import mongoengine
from decouple import config
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from starlette.requests import Request
from httpx import AsyncClient
import jwt
from datetime import datetime, timedelta
from itsdangerous import URLSafeTimedSerializer

from contextlib import asynccontextmanager

from bff_service.src.app.api import predictions_router, schedule_router
from bff_service.src.app.infrastructure.dependency_injection_container import (
    DIContainer,
)
from bff_service.src.app.models.user import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    DIContainer.initialize()

    mongoengine.connect(
        db=config("MONGO_DB"),
        host=f"mongodb://{config('MONGO_HOST')}:{config('MONGO_PORT')}/{config('MONGO_DB')}",
        username=config("MONGO_USER"),
        password=config("MONGO_PASSWORD"),
    )

    yield
    mongoengine.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(predictions_router.router, prefix="/predictions")
app.include_router(schedule_router.router, prefix="/schedule")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to BFF service"}


# auth
# Replace with your Google OAuth credentials
GOOGLE_CLIENT_ID = config("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = config("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = config("GOOGLE_REDIRECT_URI")

# Replace with your own secret key
SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(config("ACCESS_TOKEN_EXPIRE_MINUTES"))

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="https://accounts.google.com/o/oauth2/auth",
    tokenUrl="https://oauth2.googleapis.com/token",
)

serializer = URLSafeTimedSerializer(SECRET_KEY)


@app.get("/auth/google")
async def google_auth():
    return RedirectResponse(
        f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20email%20profile"
    )


@app.get("/auth/google/callback")
async def google_auth_callback(code: str):
    token_url = "https://oauth2.googleapis.com/token"

    async with AsyncClient() as client:
        token_response = await client.post(
            token_url,
            data={
                "client_id": GOOGLE_CLIENT_ID,
                "client_secret": GOOGLE_CLIENT_SECRET,
                "code": code,
                "grant_type": "authorization_code",
                "redirect_uri": GOOGLE_REDIRECT_URI,
            },
        )

        if token_response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail=f"Could not retrieve token: {token_response.text}",
            )

        token_data = token_response.json()

        user_info_response = await client.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers={"Authorization": f"Bearer {token_data['access_token']}"},
        )

        if user_info_response.status_code != 200:
            raise HTTPException(
                status_code=400,
                detail=f"Could not retrieve user info: {user_info_response.text}",
            )

        user_info = user_info_response.json()

    # Create a JWT token
    access_token = create_access_token(data=user_info)

    # Redirect to frontend with the token
    frontend_url = config("REACT_APP")  # Update this to your React app's URL
    return RedirectResponse(url=f"{frontend_url}/auth-callback?token={access_token}")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.get("/api/user")
async def get_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = User.from_dict(payload)
        if user is None or user.email is None:
            raise HTTPException(
                status_code=401, detail="Invalid authentication credentials"
            )
        # Here you would typically query your database to get the user details
        # For this example, we'll just return the email
        return user
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401, detail="Invalid authentication credentials"
        )
