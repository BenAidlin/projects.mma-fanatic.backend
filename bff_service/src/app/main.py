from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from bff_service.src.app.api import predictions_router, schedule_router
from bff_service.src.app.infrastructure.dependency_injection_container import (
    DIContainer,
)
import mongoengine
from decouple import config

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
