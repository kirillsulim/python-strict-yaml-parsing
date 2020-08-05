from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


@dataclass
class BattleStationConfig:
    @dataclass
    class Processor:
        core_count: int
        manufacturer: str

    processor: Processor
    memory_gb: int
    led_color: Optional[Color] = None
