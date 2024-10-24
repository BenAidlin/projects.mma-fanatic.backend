import abc


class AbstractTransformationService(abc.ABC):
    @abc.abstractmethod
    def transform_message(self, message: str):
        pass