from pydantic import BaseModel
import datetime as dt


class ExtractionJobModel(BaseModel):
    time = dt.datetime
    success = bool
    length = int
