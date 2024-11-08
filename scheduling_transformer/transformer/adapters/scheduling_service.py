import json
from typing import List

from ..models.mongo.event_model import EventModel
from ..services.abstract_scheduling_service import AbstractSchedulingService


class SchedulingService(AbstractSchedulingService):
    def get_current_schedule(self) -> List[dict]:
        return [json.loads(json.dumps(obj.to_mongo(), default=str)) for obj in EventModel.objects]