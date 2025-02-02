import os, logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

load_dotenv()
app_key = os.getenv("APPKEY")

from rapid.odds import ArbitrageAPI

api = ArbitrageAPI(app_key)

# Test get_arbitrage_opportunities
opps = api.get_arbitrage_opportunities()
logging.debug(opps)
