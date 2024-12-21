import threading
from typing import Any


class DIContainer:
    _services = {}
    _lock = threading.Lock()  # Create a lock for thread safety
    _initiated = False

    @classmethod
    def register(cls, key: str, service: Any):
        with cls._lock:  # Acquire the lock before modifying
            cls._services[key] = service

    @classmethod
    def resolve(cls, key: str) -> Any:
        with cls._lock:  # Acquire the lock before reading
            return cls._services.get(key)

    @classmethod
    def clear(cls) -> None:
        with cls._lock:  # Lock for clearing services
            cls._services.clear()

    @classmethod
    def is_initiated(cls) -> bool:
        with cls._lock:
            return DIContainer._initiated

    @classmethod
    def set_initiated(cls, initialized: bool) -> None:
        with cls._lock:
            DIContainer._initiated = initialized

    @classmethod
    def initialize(cls):
        # initialize di container
        DIContainer.set_initiated(True)
