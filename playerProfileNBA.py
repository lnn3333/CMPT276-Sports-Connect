import requests
import json

from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

# get full list of players
playersNBA = players.get_players()

# writing list of players to JSON file
with open("playersNBA.json", "w") as file:
    json.dump(playersNBA, file, indent=4)

with open("playersNBA.json", "r") as reading:
    data = json.load(reading)


# Lists all players in NBA in alphabetical order
def list_players():
    playersNBA = []
    for players in data:
        playersNBA.append(players["full_name"])
        sep = "\n"
        list = sep.join(playersNBA)
        
    print(list)
    
def get_players_full_name(fullname):
    player = players.find_players_by_full_name(fullname)
    playerID = player[0]["id"]
    
    playerProfile = commonplayerinfo.CommonPlayerInfo(player_id=playerID)
    pf = playerProfile.common_player_info.get_dict()
    # print(pf["data"])  
    
    player_name = pf["data"]
    for pf in player_name:
        n = pf['FIRST_NAME']
        
    print(n)
    
# function calls
# list_players()
get_players_full_name("lebron james")

        


