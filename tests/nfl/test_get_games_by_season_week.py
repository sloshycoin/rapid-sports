import os, logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

load_dotenv()
app_key = os.getenv("APPKEY")

from rapid.nfl import NFLStatsAPI

api = NFLStatsAPI(app_key)

# Test get_games_by_season_week
games_by_week = api.get_games_by_season_week(1, 1, 2021)
logging.debug(games_by_week)
