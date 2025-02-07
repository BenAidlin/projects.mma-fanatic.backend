import abc

from prediction_service.src.app.domains.prediction_domain.models.prediction_dto import (
    PredictionDto,
)


class AbstractPredictionRepository(abc.ABC):
    @abc.abstractmethod
    def create_prediction(self, prediction: PredictionDto) -> PredictionDto:
        pass

    @abc.abstractmethod
    def get_predictions(self, user_id: str) -> list[PredictionDto]:
        pass

    @abc.abstractmethod
    def update_prediction(self, prediction: PredictionDto) -> None:
        pass

    @abc.abstractmethod
    def remove_prediction(self, prediction_id: str) -> None:
        pass

