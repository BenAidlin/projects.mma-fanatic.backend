from pydantic import BaseModel
from scheduling_service.src.app.domains.schedule.models.event_model import (
    EventModel, FightModel, FighterModel)

class EventAPIModel(BaseModel):
    id: str
    name: str
    fights: list['FightAPIModel']

    @classmethod
    def from_schedule_model(cls, schedule_model: EventModel):
        fights = []
        if not schedule_model.cards:
            return None
        for c in schedule_model.cards:
            if not c.get('mtchs'):
                continue
            fights.extend([FightAPIModel.from_fight_model(f) for f in c.get('mtchs')])
        return cls(
            id=str(schedule_model.id),
            name=schedule_model.name,
            fights=fights,
        )

class FightAPIModel(BaseModel):
    id: str
    away: 'FighterAPIModel'
    home: 'FighterAPIModel'

    @classmethod
    def from_fight_model(cls, fight_model: dict):
        return cls(
            id=str(fight_model.get('id', '')),
            away=FighterAPIModel.from_fighter_model(fight_model.get('awy', {})),
            home=FighterAPIModel.from_fighter_model(fight_model.get('hme', {})),
        )


class FighterAPIModel(BaseModel):
    id: str
    country: str
    first_name: str
    last_name: str
    display_name: str
    record: str

    @classmethod
    def from_fighter_model(cls, fighter_model: dict):
        return cls(
            id=str(fighter_model.get('id')),
            country=fighter_model.get('country', ''),
            first_name=fighter_model.get('frstNm', ''),
            last_name=fighter_model.get('lstNm', ''),
            display_name=fighter_model.get('dspNm', ''),
            record=fighter_model.get('rec', ''),
        )
