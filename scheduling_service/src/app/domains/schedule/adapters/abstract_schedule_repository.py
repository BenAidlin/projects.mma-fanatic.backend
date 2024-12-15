import abc

from scheduling_service.src.app.domains.schedule.models.event_model import EventModel


class AbstractScheduleRepository:
    @abc.abstractmethod
    def get_schedule(self) -> list[EventModel]:
        pass

    @abc.abstractmethod
    def delete_event(self, event_id: int):
        pass

    @abc.abstractmethod
    def save_event(self, event: EventModel):
        pass
