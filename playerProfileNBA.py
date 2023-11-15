import requests
import json

from nba_api.stats.static import players
from nba_api.stats.endpoints import commonallplayers

# get full list of players
playersNBA = players.get_players()

# writing list of players to JSON file
with open("playersNBA.json", "w") as file:
    json.dump(playersNBA, file, indent=4)

with open("playersNBA.json", "r") as reading:
    data = json.load(reading)




