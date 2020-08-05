from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, ForwardRef


@dataclass
class BattleStationConfig:
    @dataclass
    class Processor:
        core_count: int
        manufacturer: str

    processor: ForwardRef("Processor")
    memory_gb: int
    led_color: Optional["Color"] = field(default=None, metadata={"by_value": True})


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
