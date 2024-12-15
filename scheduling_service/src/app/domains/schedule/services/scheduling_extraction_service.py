import abc
import datetime as dt
from scheduling_service.src.app.domains.schedule.adapters.abstract_data_extractor import AbstractDataExtractor
from scheduling_service.src.app.domains.schedule.adapters.abstract_schedule_repository import (
    AbstractScheduleRepository,
)
from scheduling_service.src.app.infrastructure.dependency_injection_container import DIContainer
from scheduling_service.src.app.domains.schedule.models.event_model import EventModel

class AbstractSchedulingExtractionService:
    @abc.abstractmethod
    def extract_general_schedule(self):
        pass

    @abc.abstractmethod
    def get_schedule(self) -> list[EventModel]:
        pass

class SchedulingExtractionService(AbstractSchedulingExtractionService):
    DATETIME_FORMAT = "%Y-%m-%dT%H:%MZ"
    def __init__(
        self,
        abstract_data_extractor: AbstractDataExtractor = None,
        abstract_scheduling_repository: AbstractScheduleRepository = None,
    ):
        self.abstract_data_extractor: AbstractDataExtractor = (
            abstract_data_extractor or DIContainer.resolve("AbstractDataExtractor")
        )
        self.abstract_schedule_repository: AbstractScheduleRepository = (
            abstract_scheduling_repository
            or DIContainer.resolve("AbstractScheduleRepository")
        )

    def extract_general_schedule(self):
        new_events = self.abstract_data_extractor.extract_data()
        # keep only relevant events
        new_events = [event for event in new_events if event.cards and event.event_date]
        current_schedule = self.get_schedule()
        for event in current_schedule:
            if event.event_date.year >= dt.datetime.now().year:
                self.abstract_schedule_repository.delete_event(event_id=event.id)
        for event in new_events:
            self.abstract_schedule_repository.save_event(event)

    def get_schedule(self) -> list[EventModel]:
        return self.abstract_schedule_repository.get_schedule()
