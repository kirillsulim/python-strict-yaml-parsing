from pprint import pprint

from yaml import load, SafeLoader

from config_with_tag import BattleStationConfig


yaml = """
--- !BattleStationConfig
processor: !Processor
  core_count: 8
  manufacturer: Intel
memory_gb: 8
led_color: red
"""

a = BattleStationConfig

loaded = load(yaml, Loader=SafeLoader)
pprint(loaded)
