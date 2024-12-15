from pydantic import BaseModel
import datetime as dt


class FighterStats(BaseModel):
    age: int | None | str
    ht: str | None
    rch: str | None
    sigstrkacc: str | None
    sigstrklpm: str | None
    stnce: str | None
    subavg: str | None
    tdacc: str | None
    tdavg: str | None
    wt: str | None
    odds: str | None


class FighterModel(BaseModel):
    original_id: str | None
    gender: str
    country: str | None
    first_name: str | None
    last_name: str | None
    display_name: str | None
    rec: str | None
    short_display_name: str | None
    stats: FighterStats | None


class FightModel(BaseModel):
    original_id: str | None
    awy: FighterModel
    hme: FighterModel
    nte: str | None
    status: str | None
    dt: dt.datetime | None


class CardModel(BaseModel):
    hdr: str | None
    status: str | None
    mtchs: list[FightModel] | None


class EventModel(BaseModel):
    id: str | None
    original_id: str
    is_completed: bool
    postponed_or_canceled: bool
    event_date: dt.datetime
    name: str
    cards: list[CardModel] | None
