from threading import Thread

from django.apps import AppConfig

from common.adapters.abstract_msg_client import AbstractMsgClient
from .dependency_injection_service import DIService


class TransformerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transformer'

    def ready(self):
        consumer: AbstractMsgClient = DIService.resolve('AbstractMsgClient')
        consumer_thread = Thread(target=consumer.consume_messages, args=(TransformerConfig._consumer_callback,))
        consumer_thread.daemon = True
        consumer_thread.start()

    @staticmethod
    def _consumer_callback(message):
        print(message)

