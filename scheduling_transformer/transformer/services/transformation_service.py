import json
from ..adapters.abstract_transformation_service import AbstractTransformationService
from ..models.mongo.event_model import EventModel

class TransformationService(AbstractTransformationService):
    def __init__(self):
        pass
    def transform_message(self, message: str):
        events = [EventModel(**event) for event in json.loads(message) if isinstance(event, dict)]
        for event in events:
            event.save()

