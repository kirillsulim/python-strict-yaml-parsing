from dataclasses import dataclass
from enum import Enum
from typing import Optional

from yaml import YAMLObject, SafeLoader


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


@dataclass
class BattleStationConfig(YAMLObject):
    yaml_tag = "!BattleStationConfig"
    yaml_loader = SafeLoader

    @dataclass
    class Processor(YAMLObject):
        yaml_tag = "!Processor"
        yaml_loader = SafeLoader

        core_count: int
        manufacturer: str

    processor: Processor
    memory_gb: int
    led_color: Optional[Color] = None
