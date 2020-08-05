from pprint import pprint

from yaml import load, SafeLoader

from config import BattleStationConfig


yaml = """
processor:
  core_count: 8
  manufacturer: Intel
memory_gb: 8
led_color: red
"""

loaded = load(yaml, Loader=SafeLoader)
pprint(loaded)

parsed_config = BattleStationConfig(**loaded)
pprint(parsed_config)