import asyncio
from contextlib import asynccontextmanager
import threading
from fastapi import FastAPI
import mongoengine
from decouple import config

from fight_service.src.app.infrastructure.dependency_injection_container import (
    DIContainer,
)
from fight_service.src.app.infrastructure.kafka_client import AbstractMsgClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    mongoengine.connect(
        db=config("MONGO_DB"),
        host=f"mongodb://{config('MONGO_HOST')}:{config('MONGO_PORT')}/{config('MONGO_DB')}",
        username=config("MONGO_USER"),
        password=config("MONGO_PASSWORD"),
    )
    DIContainer.initialize()
    msg_client: AbstractMsgClient = DIContainer.resolve("AbstractMsgClient")
    thread = threading.Thread(
        target=msg_client.consume_messages,
        args=(lambda message: print(f"Received message: {message}"),),
        daemon=True,
    )
    thread.start()
    yield
    mongoengine.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}
