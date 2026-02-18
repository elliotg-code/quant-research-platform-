from dataclasses import dataclass
from enum import Enum, auto
from datetime import datetime


class EventType(Enum):
    MARKET = auto()
    SIGNAL = auto()
    ORDER = auto()
    FILL = auto()


@dataclass(frozen=True)
class Event:
    type: EventType
    timestamp: datetime
