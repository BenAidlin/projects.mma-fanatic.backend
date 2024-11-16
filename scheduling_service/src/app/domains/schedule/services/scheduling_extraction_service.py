import abc

from scheduling_service.src.app.domains.schedule.adapters.abstract_data_extractor import AbstractDataExtractor
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
    def __init__(self, abstract_data_extractor: AbstractDataExtractor=None):
        self.abstract_data_extractor: AbstractDataExtractor = abstract_data_extractor
        if not self.abstract_data_extractor:
            self.abstract_data_extractor = DIContainer.resolve('AbstractDataExtractor')

    def extract_general_schedule(self):
        raw_data = self.abstract_data_extractor.extract_data()
        schedule = [EventModel(**event).save() for event in raw_data]

    def get_schedule(self) -> list[EventModel]:
        return EventModel.get_data()