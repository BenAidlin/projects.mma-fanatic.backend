from typing import Union, Optional, Callable
from kafka import KafkaProducer, KafkaConsumer
import abc


class AbstractMsgClient(abc.ABC):
    @abc.abstractmethod
    def produce_message(self, message: str) -> None:
        pass

    @abc.abstractmethod
    def consume_messages(self, callback) -> str:
        pass


class KafkaClient(AbstractMsgClient):
    def __init__(
        self,
        bootstrap_servers: Union[str, list],
        topic: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
    ):
        try:
            self._bootstrap_servers = bootstrap_servers
            self._topic = topic
            self.username = username
            self.password = password
            if self.username and self.password:
                self._producer = KafkaProducer(
                    bootstrap_servers=bootstrap_servers,
                    security_protocol="SASL_PLAINTEXT",
                    sasl_mechanism="PLAIN",
                    sasl_plain_username=username,
                    sasl_plain_password=password,
                )
            else:  # no authentication
                self._producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
        except Exception as e:
            pass

    def produce_message(self, message: str) -> None:
        self._producer.send(self._topic, message.encode("utf-8"))
        self._producer.flush()

    def consume_messages(self, callback: Callable[[str], None]) -> None:
        if self.username and self.password:
            consumer = KafkaConsumer(
                self._topic,
                bootstrap_servers=self._bootstrap_servers,
                auto_offset_reset="earliest",  # Start reading at the earliest message
                enable_auto_commit=True,
                group_id="my-group",  # Consumer group ID
                value_deserializer=lambda x: x.decode("utf-8"),  # Decode the message
                security_protocol="SASL_PLAINTEXT",
                sasl_mechanism="PLAIN",
                sasl_plain_username=self.username,
                sasl_plain_password=self.password,
            )
        else:  # no authentication
            consumer = KafkaConsumer(
                self._topic,
                bootstrap_servers=self._bootstrap_servers,
                auto_offset_reset="earliest",  # Start reading at the earliest message
                enable_auto_commit=True,
                group_id="my-group",  # Consumer group ID
                value_deserializer=lambda x: x.decode("utf-8"),  # Decode the message
            )
        for message in consumer:
            callback(message.value)

    def close_producer(self) -> None:
        self._producer.close()
