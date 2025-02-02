# RapidAPI Python Project

This project provides Python wrappers for various sports-related APIs available on RapidAPI. The APIs included are for arbitrage opportunities, sports odds, and NFL statistics.

## Installation

To clone this repository, run:

```bash
git clone https://github.com/sloshycoin/rapid.git
cd rapid
```

To install the `rapid` package, run:

```bash
pip install .
```

Alternatively, you can use `pdm` to manage dependencies and install the package:

1. Install `pdm` if you haven't already:

    ```bash
    pip install pdm
    ```

2. Use `pdm` to install the dependencies and the package:

    ```bash
    pdm install
    ```

## Usage

### ArbitrageAPI

The `ArbitrageAPI` class provides methods to fetch arbitrage opportunities.

#### Example

```python
from rapid.odds.api import ArbitrageAPI

api_key = "your_api_key"
arbitrage_api = ArbitrageAPI(api_key)
opportunities = arbitrage_api.get_arbitrage_opportunities()
print(opportunities)
```

### OddsAPI

The `OddsAPI` class provides methods to fetch sports odds and list active sports.

#### Example

```python
from rapid.odds.api import OddsAPI

api_key = "your_api_key"
odds_api = OddsAPI(api_key)
sports = odds_api.get_sports()
print(sports)

odds = odds_api.get_odds_by_sport(sport="soccer")
print(odds)
```

### NFLStatsAPI

The `NFLStatsAPI` class provides methods to fetch NFL game, player, and team statistics.

#### Example

```python
from rapid.nfl.api import NFLStatsAPI

api_key = "your_api_key"
nfl_api = NFLStatsAPI(api_key)
game_info = nfl_api.get_game_by_id(game_id="12345")
print(game_info)

player_info = nfl_api.get_player_info_by_id(player_id="67890")
print(player_info)

team_info = nfl_api.get_team_by_id(team_id="team123")
print(team_info)
```

## License

This project is licensed under the MIT License.
