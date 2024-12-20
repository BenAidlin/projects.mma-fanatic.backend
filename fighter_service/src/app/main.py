from fastapi import FastAPI
from mongoengine import connect
from decouple import config

from fighter_service.src.app.infrastructure.dependency_injection_container import (
    DIContainer,
)
from fighter_service.src.app.infrastructure.kafka_client import AbstractMsgClient

connect(
    db=config("MONGO_DB"),
    host=f"mongodb://{config('MONGO_HOST')}:{config('MONGO_PORT')}/{config('MONGO_DB')}",
    username=config("MONGO_USER"),
    password=config("MONGO_PASSWORD"),
)

app = FastAPI()


@app.on_event("startup")
def startup_event():
    DIContainer.initialize()
    msg_client: AbstractMsgClient = DIContainer.resolve("AbstractMsgClient")
    msg_client.consume_messages(lambda message: print(f"Received message: {message}"))


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}
