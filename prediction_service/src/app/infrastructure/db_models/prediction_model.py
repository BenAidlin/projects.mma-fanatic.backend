import mongoengine as me

from prediction_service.src.app.domains.prediction_domain.models.prediction_dto import (
    Method,
    PredictionDto,
)


class PredictionModelDb(me.Document):
    user_id = me.StringField(required=True, null=False)
    winner = me.StringField(required=False, null=True)
    method = me.StringField(required=False, null=True)
    round = me.IntField(required=False, null=True)
    potential_gain = me.IntField(required=False, null=True)
    hme_id = me.StringField(required=True, null=False)
    awy_id = me.StringField(required=True, null=False)
    meta = {
        "collection": "predictions",
        "strict": False,
    }

    @classmethod
    def get_data(cls):
        return cls.objects()

    def to_pydantic(self):
        return PredictionDto(
            prediction_id=str(self.pk),
            user_id=self.user_id,
            winner=self.winner,
            method=Method(self.method),
            round=self.round,
            potential_gain=self.potential_gain,
            hme_id=self.hme_id,
            awy_id=self.awy_id,
        )

    @classmethod
    def from_pydantic(cls, pydantic_model: PredictionDto):
        return PredictionModelDb(
            user_id=pydantic_model.user_id,
            winner=pydantic_model.winner,
            method=pydantic_model.method.name,
            round=pydantic_model.round,
            potential_gain=pydantic_model.potential_gain,
            hme_id=pydantic_model.hme_id,
            awy_id=pydantic_model.awy_id,
        )
