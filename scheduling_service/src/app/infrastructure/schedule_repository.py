from scheduling_service.src.app.domains.schedule.adapters.abstract_schedule_repository import (
    AbstractScheduleRepository,
)
from scheduling_service.src.app.domains.schedule.models.event_model import EventModel
from scheduling_service.src.app.infrastructure.db_models import db_event_model


class ScheduleRepository(AbstractScheduleRepository):
    def get_schedule(self) -> list[EventModel]:
        db_data: list[db_event_model.EventModelDb] = (
            db_event_model.EventModelDb.get_data()
        )
        return [db_event.to_pydantic() for db_event in db_data]

    def delete_event(self, event_id: str):
        db_event_model.EventModelDb.objects(id=event_id).delete()

    def save_event(self, event: EventModel):
        event_db_model = db_event_model.EventModelDb.from_pydantic(event)
        event_db_model.save()
