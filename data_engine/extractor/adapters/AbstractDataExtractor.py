import abc


class AbstractDataExtractor(abc.ABC):
    @abc.abstractmethod
    def extract_data(self):
        pass