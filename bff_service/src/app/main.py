from contextlib import asynccontextmanager
from fastapi import FastAPI

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


@app.get("/")
def read_root():
    return {"message": "Welcome to BFF service"}
