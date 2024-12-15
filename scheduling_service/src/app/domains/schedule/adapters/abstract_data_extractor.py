import abc

from scheduling_service.src.app.domains.schedule.models.event_model import EventModel


class AbstractDataExtractor(abc.ABC):
    @abc.abstractmethod
    def extract_data(self) -> list[EventModel]:
        pass
