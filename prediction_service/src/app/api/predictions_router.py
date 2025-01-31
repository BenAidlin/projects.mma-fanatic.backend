from fastapi import APIRouter
from fastapi_restful.cbv import cbv

from prediction_service.src.app.domains.prediction_domain.facade.prediction_facade import (
    PredictionFacade,
)
from prediction_service.src.app.domains.prediction_domain.models.prediction_dto import (
    PredictionDto,
)
from prediction_service.src.app.infrastructure.dependency_injection_container import (
    DIContainer,
)

router = APIRouter()


@cbv(router)
class PredictionAPI:
    def __init__(self):
        self.prediction_facade: PredictionFacade = DIContainer.resolve(
            "PredictionFacade"
        )

    @router.post("/")
    def create_prediction(self, prediction: PredictionDto):
        return self.prediction_facade.create_prediction(prediction)

    @router.get("/{user_id}")
    def get_predictions(self, user_id: str):
        return self.prediction_facade.get_predictions(user_id)

    @router.put("/")
    def update_prediction(self, prediction: PredictionDto):
        self.prediction_facade.update_prediction(prediction)
        return {"message": "Predictions updated successfully"}

    @router.delete("/")
    def remove_predictions(self, predictions: list[PredictionDto]):
        self.prediction_facade.remove_predictions(predictions)
        return {"message": "Predictions removed successfully"}
