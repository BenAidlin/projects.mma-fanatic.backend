import abc
from typing import List

from ..models.mongo.event_model import EventModel


class AbstractSchedulingService(abc.ABC):
    @abc.abstractmethod
    def get_current_schedule(self) -> List[EventModel]:
        pass