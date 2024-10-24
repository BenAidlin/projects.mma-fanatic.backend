from common.implementations.dependency_injection_container import DIContainer
import threading

class DIService(DIContainer):
    @classmethod
    def initialize(cls):
        from decouple import config
        from common.implementations.kafka_client import KafkaClient

        DIService.register('AbstractMsgClient',
                             KafkaClient(
                                 config('KAFKA_BOOTSTRAP_SERVERS'),
                                 config('KAFKA_TOPIC'),
                                 config('KAFKA_USER'),
                                 config('KAFKA_PASSWORD')))


lock = threading.Lock()
with lock:
    if not DIService.is_initiated():
        DIService.initialize()
        DIService._initiated = True