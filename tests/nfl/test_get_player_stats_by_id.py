import os, logging
from json import dump
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

load_dotenv()
app_key = os.getenv("APPKEY")

from rapid.nfl import NFLStatsAPI

api = NFLStatsAPI(app_key)

# Test get_player_stats_by_id
player_stats = api.get_player_stats_by_id("16802", 2024)
logging.debug(player_stats)
with open('player_Stats.json', 'w') as f:
    dump(player_stats, f, indent=4)
    logging.debug("Wrote teams to tests/nfl/teams.json")
