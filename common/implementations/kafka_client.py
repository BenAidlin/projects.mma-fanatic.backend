from typing import Union, Optional, Callable

from common.adapters.abstract_msg_client import AbstractMsgClient
from kafka import KafkaProducer, KafkaConsumer


class KafkaClient(AbstractMsgClient):
    def __init__(self, bootstrap_servers: Union[str, list], topic: str):
        self._bootstrap_servers = bootstrap_servers
        self._topic = topic
        self._producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    def produce_message(self, message: str) -> None:
        self._producer.send(self._topic, message.encode('utf-8'))
        self._producer.flush()

    def consume_messages(self, callback: Callable[[str], None]) -> None:
        consumer = KafkaConsumer(
            self._topic,
            bootstrap_servers=self._bootstrap_servers,
            auto_offset_reset='earliest',  # Start reading at the earliest message
            enable_auto_commit=True,
            group_id='my-group',  # Consumer group ID
            value_deserializer=lambda x: x.decode('utf-8')  # Decode the message
        )
        print("Starting to consume messages...")
        for message in consumer:
            callback(message.value)

    def close_producer(self) -> None:
        self._producer.close()