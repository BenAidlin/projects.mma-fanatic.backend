from common.dependency_injection_container import DIContainer
from .adapters.scheduling_service import SchedulingService
from .adapters.transformation_service import TransformationService
import threading

class DIService(DIContainer):
    @classmethod
    def initialize(cls):
        from decouple import config
        from common.adapters.kafka_client import KafkaClient

        DIService.register('AbstractMsgClient',
                             KafkaClient(
                                 config('KAFKA_BOOTSTRAP_SERVERS'),
                                 config('KAFKA_TOPIC'),
                                 config('KAFKA_USER'),
                                 config('KAFKA_PASSWORD')))

        DIService.register('AbstractTransformationService', TransformationService())
        DIService.register('AbstractSchedulingService', SchedulingService())

lock = threading.Lock()
with lock:
    if not DIService.is_initiated():
        DIService.initialize()
        DIService._initiated = True