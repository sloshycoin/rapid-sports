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

# Test get_team_by_id
players = api.get_team_players_by_id("26")
with open('team_Players.json', 'w') as f:
    dump(players, f, indent=4)
    logging.debug("Wrote teams to tests/nfl/teams.json")
