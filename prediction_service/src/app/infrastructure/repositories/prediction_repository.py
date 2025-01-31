from prediction_service.src.app.domains.prediction_domain.adapters.abstract_prediction_repository import (
    AbstractPredictionRepository,
)
from prediction_service.src.app.domains.prediction_domain.models.prediction_dto import (
    PredictionDto,
)
from prediction_service.src.app.infrastructure.db_models.prediction_model import (
    PredictionModelDb,
)


class PredictionRepository(AbstractPredictionRepository):
    def create_prediction(self, prediction: PredictionDto) -> PredictionDto:
        prediction_db = PredictionModelDb.from_pydantic(prediction)
        prediction_db.save()
        return prediction_db.to_pydantic()

    def get_predictions(self, user_id: str) -> list[PredictionDto]:
        return [
            prediction.to_pydantic()
            for prediction in PredictionModelDb.objects(user_id=user_id)
        ]

    def update_prediction(self, prediction: PredictionDto) -> None:
        prediction_model = PredictionModelDb.objects(
            id=prediction.prediction_id
        ).first()
        if not prediction_model:
            return
        prediction_model.user_id = prediction.user_id
        prediction_model.winner = prediction.winner
        prediction_model.method = prediction.method.name
        prediction_model.round = prediction.round
        prediction_model.potential_gain = prediction.potential_gain
        prediction_model.save()

    def remove_prediction(self, prediction_id: str) -> None:
        prediction_model = PredictionModelDb.objects(id=prediction_id).first()
        if prediction_model:
            prediction_model.delete()
