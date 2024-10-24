from ..adapters.abstract_transformation_service import AbstractTransformationService

class TransformationService(AbstractTransformationService):
    def __init__(self):
        pass
    def transform_message(self, message: str):
        print(message)

