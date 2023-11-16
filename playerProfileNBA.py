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

# Retrieves player ID
def get_playerID(player):
    player = players.find_players_by_full_name(player)
    playerID = player[0]["id"]
    return playerID
    
def get_players_full_name(fullname):
   
    playerID = get_playerID(fullname)
    
    playerProfile = commonplayerinfo.CommonPlayerInfo(player_id=playerID)
    pf = playerProfile.get_normalized_json()
    
    jsonobj = json.loads(pf) # converts json string to json object

    # writing player info to JSON file
    with open("playersProfileNBA.json", "w") as file:
        json.dump(jsonobj, file, indent=4)

    with open("playersProfileNBA.json", "r") as reading:
        datapf = json.load(reading)
        
    for info in datapf["CommonPlayerInfo"]:
        name = "Player: " + info["DISPLAY_FIRST_LAST"]
        bday = "Birthday: " + info["BIRTHDATE"]
        height = "Height: " + info["HEIGHT"]
        weight = "Weight: " + info["WEIGHT"]
        country = "Country: " + info["COUNTRY"]
        jersey = "Jersey: " + info["JERSEY"]
        pos = "Position: " + info["POSITION"]
        team = "Team: " + info["TEAM_NAME"]

    display_player_profile(name, height, weight, bday, country, jersey, pos, team)

# helper function to display player's profile
def display_player_profile(pName, pHeight, pWeight, pBday, pCountry, pJersey, pPos, pTeam):
    pf_arr = []
    
    pf_arr.append(pName)
    pf_arr.append(pHeight)
    pf_arr.append(pWeight)
    pf_arr.append(pBday)
    pf_arr.append(pCountry)
    pf_arr.append(pJersey)
    pf_arr.append(pPos)
    pf_arr.append(pTeam)
    
    sep = "\n"
    display = sep.join(pf_arr)
    print(display)
    
    
# function calls
# list_players()
get_players_full_name("lebron james")
# get_playerID("lebron james")
        


