import requests

class ArbitrageAPI:
    def __init__(self, api_key: str):
        self.host = "sportsbook-api2.p.rapidapi.com"
        self.url = f"https://{self.host}"
        self.__headers = {"x-rapidapi-host": self.host, "x-rapidapi-key": api_key}

    def __str__(self):
        return f"Arbitrage API via RapidAPI @ {self.url}"

    def get_arbitrage_opportunities(self):
        url = f"{self.url}/v0/advantages"
        response = requests.get(url, headers=self.__headers, params={"type": "ARBITRAGE"})
        return response.json()

class OddsAPI:
    def __init__(self, api_key: str):
        self.host = "odds.p.rapidapi.com"
        self.url = f"https://{self.host}"
        self.__headers = {"x-rapidapi-host": self.host, "x-rapidapi-key": api_key}

    def __str__(self):
        return f"Odds API via RapidAPI @ {self.url}"

    def get_odds_by_sport(self, sport: str, market: str = None, region: str = "us", odds_format: str = "decimal", date_format: str = "iso"):
        url = f"{self.url}v4/sports/{sport}/odds"
        data = {"regions": region, "oddsFormat": odds_format, "dateFormat": date_format}
        if market:
            data["markets"] = market
        response = requests.get(url, headers=self.__headers, params={"sport": sport})
        return response.json()

    def get_sports(self):
        url = f"{self.url}/v4/sports"
        response = requests.get(url, headers=self.__headers, params={"all": "true"})
        return response.json()

    def list_active_sports(self):
        all_sports = self.get_sports()
        active_sports = [sport for sport in all_sports if sport["active"]]
        self.active_sports = active_sports
        self.sports_keys = [sport["key"] for sport in active_sports]
