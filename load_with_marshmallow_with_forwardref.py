from pprint import pprint
from typing import Type, Any

from yaml import load, SafeLoader
from marshmallow_dataclass import class_schema

from config_for_marshmallow_with_forwardref import BattleStationConfig


yaml = """
processor:
  core_count: 8
  manufacturer: Intel
memory_gb: 8
led_color: red
"""

loaded = load(yaml, Loader=SafeLoader)
pprint(loaded)

BattleStationConfigSchema = class_schema(BattleStationConfig)

result = BattleStationConfigSchema().load(loaded)
pprint(result)


def strict_load_yaml(yaml: str, loaded_type: Type[Any]):
    schema = class_schema(loaded_type)
    return schema().load(load(yaml, Loader=SafeLoader))


pprint(strict_load_yaml(yaml, BattleStationConfig))
