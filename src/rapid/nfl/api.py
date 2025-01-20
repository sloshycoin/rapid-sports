import requests

class NFLStatsAPI:
    def __init__(self, api_key: str):
        self.host = "nfl-api-data.p.rapidapi.com"
        self.url = f"https://{self.host}"
        self.__headers = {"x-rapidapi-host": self.host, "x-rapidapi-key": api_key}

    def __str__(self):
        return f"NFL Stats API via RapidAPI @ {self.url}"

    ## GAMES ##

    def get_game_by_id(self, game_id: str):
        url = f"{self.url}/nfl-single-events"
        data = {"id": game_id}
        response = requests.get(url, headers=self.__headers, params=data)
        return response.json()

    def get_game_boxscore_by_id(self, game_id: str):
        url = f"{self.url}/nfl-boxscore"
        data = {"id": game_id}
        response = requests.get(url, headers=self.__headers, params=data)
        return response.json()

    def get_game_play_by_play_by_id(self, game_id: str):
        url = f"{self.url}/nfl-plays"
        data = {"id": game_id}
        response = requests.get(url, headers=self.__headers, params=data)
        return response.json()

    def get_games_by_season_week(self, season: int, week: int, year: int):
        url = f"{self.url}/nfl-weeks-events"
        data = {"type": f"{season}", "week": f"{week}", "year": f"{year}"}
        response = requests.get(url, headers=self.__headers, params=data)
        return response.json()

    def get_games_by_year(self, year: int):
        url = f"{self.url}/nfl-events"
        data = {"year": f"{year}"}
        response = requests.get(url, headers=self.__headers, params=data)
        return response.json()

    ## PLAYERS ##

    def get_player_info_by_id(self, player_id: str):
        url = f"{self.url}/nfl-ath-fullinfo"
        data = {"id": player_id}
        response = requests.get(url, headers=self.__headers, params=data)
        return response.json()

    def get_player_news_by_id(self, player_id: str):
        url = f"{self.url}/nfl-ath-news"
        data = {"id": player_id}
        response = requests.get(url, headers=self.__headers, params=data)
        return response.json()

    def get_player_notes_by_id(self, player_id: str):
        url = f"{self.url}/nfl-ath-notes"
        data = {"id": player_id}
        response = requests.get(url, headers=self.__headers, params=data)
        return response.json()

    def get_player_stats_by_id(self, player_id: str, year: int = None):
        url = f"{self.url}/nfl-ath-stats"
        data = {"id": player_id}
        if year:
            data["year"] = f"{year}"
        response = requests.get(url, headers=self.__headers, params=data)
        return response.json()

    ## TEAMS ##

    def get_team_by_id(self, team_id: str):
        url = f"{self.url}/nfl-team-info/v1/data"
        data = {"id": team_id}
        response = requests.get(url, headers=self.__headers, params=data)
        return response.json()

    def get_team_stats_by_id(self, team_id: str, year: int):
        url = f"{self.url}/nfl-team-statistics"
        data = {"id": team_id, "year": f"{year}"}
        response = requests.get(url, headers=self.__headers, params=data)
        return response.json()

    def get_teams(self) -> list:
        url = f"{self.url}/nfl-team-listing/v1/data"
        response = requests.get(url, headers=self.__headers)
        return response.json()
