from prediction_service.src.app.domains.prediction_domain.models.prediction_dto import (
    PredictionDto,
)
from prediction_service.src.app.domains.prediction_domain.service.prediction_service import (
    PredictionService,
)
from prediction_service.src.app.infrastructure.dependency_injection_container import (
    DIContainer,
)


class PredictionFacade:
    def __init__(self):
        self.prediction_service: PredictionService = DIContainer.resolve(
            "PredictionService"
        )

    def create_prediction(self, prediction_dto: PredictionDto) -> PredictionDto:
        return self.prediction_service.create_prediction(prediction_dto)

    def get_predictions(self, user_id: str) -> list[PredictionDto]:
        return self.prediction_service.get_predictions(user_id)

    def update_prediction(self, prediction: PredictionDto):
        self.prediction_service.update_prediction(prediction)

    def remove_predictions(self, predictions: list[PredictionDto]) -> None:
        self.prediction_service.remove_predictions(predictions)
