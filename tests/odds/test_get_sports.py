import os, logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

load_dotenv()
app_key = os.getenv("APPKEY")

from rapid.odds import OddsAPI

api = OddsAPI(app_key)

# Test get_sports **called by list_active_sports**
# sports = api.get_sports()
# logging.debug(sports)

# Test list_active_sports
api.list_active_sports()
logging.debug(api.sports_keys)
logging.debug(f"Active Count: {len(api.active_sports)}")
