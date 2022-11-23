from abc import ABC, abstractmethod


class CustomAPI(ABC):
    @abstractmethod
    def print_message(self, msg: str) -> None:
        pass
