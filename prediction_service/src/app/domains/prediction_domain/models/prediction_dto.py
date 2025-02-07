from pydantic import BaseModel
from enum import Enum


class Method(Enum):
    NOT_PICKED = "NOT_PICKED"
    KO = "KO"
    SUB = "SUB"
    DEC = "DEC"


class PredictionDto(BaseModel):
    prediction_id: str | None
    user_id: str
    winner: str | None
    method: Method
    round: int | None
    potential_gain: int | None
    # fight identifiers
    hme_id: str
    awy_id: str
