import threading
from mimetypes import inited
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
        return DIContainer._initiated

    @classmethod
    def set_initiated(cls, initialized: bool) -> None:
        DIContainer._initiated = initialized

    @classmethod
    def initialize(cls) -> None:
        raise NotImplementedError("Subclasses must implement the initialize method.")
