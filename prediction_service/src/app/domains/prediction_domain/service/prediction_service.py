from prediction_service.src.app.domains.prediction_domain.adapters.abstract_prediction_repository import (
    AbstractPredictionRepository,
)
from prediction_service.src.app.domains.prediction_domain.models.prediction_dto import (
    PredictionDto,
)
from prediction_service.src.app.infrastructure.dependency_injection_container import (
    DIContainer,
)


class PredictionService:
    def __init__(self, prediction_repo: AbstractPredictionRepository = None):
        self.prediction_repo: AbstractPredictionRepository = (
            prediction_repo or DIContainer.resolve("AbstractPredictionRepository")
        )

    def create_prediction(self, prediction_dto: PredictionDto) -> PredictionDto:
        return self.prediction_repo.create_prediction(prediction_dto)

    def get_predictions(self, user_id: str) -> list[PredictionDto]:
        return self.prediction_repo.get_predictions(user_id)

    def update_prediction(self, prediction: PredictionDto) -> None:
        return self.prediction_repo.update_prediction(prediction)

    def remove_predictions(self, predictions: list[PredictionDto]) -> None:
        for prediction in predictions:
            self.prediction_repo.remove_prediction(prediction.prediction_id)
