from abc import ABC, abstractmethod
from backtester.core.event import Event

class BaseStrategy(ABC):
    @abstractmethod
    def on_event(self, event: Event) -> None:
        pass
