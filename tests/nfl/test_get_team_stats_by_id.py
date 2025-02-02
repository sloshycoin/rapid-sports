import os, logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

load_dotenv()
app_key = os.getenv("APPKEY")

from rapid.nfl import NFLStatsAPI

api = NFLStatsAPI(app_key)

# Test get_team_stats_by_id
team_stats = api.get_team_stats_by_id("team_id_example", 2021)
logging.debug(team_stats)
