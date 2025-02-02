import os, logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

load_dotenv()
app_key = os.getenv("APPKEY")

from rapid.odds import OddsAPI

api = OddsAPI(app_key)

# Test get_odds_by_sport
odds = api.get_odds_by_sport("americanfootball_nfl")
logging.debug(odds)
