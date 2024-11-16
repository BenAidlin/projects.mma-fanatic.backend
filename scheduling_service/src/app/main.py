from fastapi import FastAPI

from scheduling_service.src.app.infrastructure.dependency_injection_container import DIContainer
from scheduling_service.src.app.api.v1 import schedule_router
from mongoengine import connect
from decouple import config

DIContainer.initialize()

connect(
    db=config('MONGO_DB'),
    host=f"mongodb://{config('MONGO_HOST')}:{config('MONGO_PORT')}/{config('MONGO_DB')}",
    username=config('MONGO_USER'),
    password=config('MONGO_PASSWORD'),
)

app = FastAPI()
app.include_router(schedule_router.router, prefix='/schedule')

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}
