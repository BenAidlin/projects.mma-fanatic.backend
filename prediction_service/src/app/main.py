from contextlib import asynccontextmanager
from fastapi import FastAPI

from prediction_service.src.app.api import predictions_router
from prediction_service.src.app.domains.prediction_domain.adapters.abstract_msg_client import (
    AbstractMsgClient,
)
from prediction_service.src.app.domains.prediction_domain.facade.prediction_facade import (
    PredictionFacade,
)
from prediction_service.src.app.infrastructure.dependency_injection_container import (
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


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}
