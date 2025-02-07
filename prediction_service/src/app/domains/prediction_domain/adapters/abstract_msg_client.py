import abc


class AbstractMsgClient(abc.ABC):
    @abc.abstractmethod
    def produce_message(self, message: str) -> None:
        pass

    @abc.abstractmethod
    def consume_messages(self, callback) -> str:
        pass
