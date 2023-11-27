import requests
import json

from datetime import datetime
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

# get full list of players
playersNBA = players.get_players()

# writing list of players to JSON file
with open("playersNBA.json", "w") as file:
    json.dump(playersNBA, file, indent=4)

def readDataPlayer():
    with open("playersNBA.json", "r") as reading:
        dataPlayer = json.load(reading)
    return dataPlayer

# Lists all players in NBA in alphabetical order
def list_players():
    playersNBA = []
    data = readDataPlayer()
    for players in data:
        playersNBA.append(players["full_name"])
        sep = "\n"
        list = sep.join(playersNBA)
        
    return list

# Retrieves player ID
def get_playerID(player):
    player = players.find_players_by_full_name(player)
    playerID = player[0]["id"]
    return playerID

# retreives player info by first name
def get_players_by_first_name(firstname):
    
    player = players.find_players_by_first_name(firstname)
    data = readDataPlayer()
    # print(player)
    
    player_count = 0
    player_dict = {}
    
    for plr in data:
        if player[player_count-1]["first_name"] == plr["first_name"]:
            player_count += 1
            player_dict[str(player_count)] = (plr["id"], plr["full_name"])
            
    if player_count > 1:
        
        for key, tuple in player_dict.items():
            print(f"{key}: {tuple[1]}")
            
        chosenPlayer = input("\nPlease choose a player: ")
        if chosenPlayer in player_dict:
            get_players_full_name(player_dict[chosenPlayer][1])
    
    else:
        get_players_full_name(player[0]["full_name"])
        
# retrieves player info by last name
def get_players_by_last_name(lastname):
    
    player = players.find_players_by_last_name(lastname)
    data = readDataPlayer()
    # print(player)
     
    player_count = 0
    player_dict = {}
    
    for plr in data:
        if player[player_count-1]["last_name"] == plr["last_name"]:
            player_count += 1
            player_dict[str(player_count)] = (plr["id"], plr["full_name"])
            
    if player_count > 1:
        
        for key, tuple in player_dict.items():
            print(f"{key}: {tuple[1]}")
            
        chosenPlayer = input("\nPlease choose a player: ")
        if chosenPlayer in player_dict:
            get_players_full_name(player_dict[chosenPlayer][1])
    
    else:
        get_players_full_name(player[0]["full_name"])
    

# retrieves player info by full name
def get_players_full_name(fullname):
   
    playerID = get_playerID(fullname)
    
    playerProfile = commonplayerinfo.CommonPlayerInfo(player_id=playerID)
    pf = playerProfile.get_normalized_json()
    
    jsonobj = json.loads(pf) # converts json string to json object

    player_info = {}
    for info in jsonobj["CommonPlayerInfo"]:
        player_info["name"] = info["DISPLAY_FIRST_LAST"]
        player_info["bday"] = formatDate(info["BIRTHDATE"])
        player_info["height"] = modifyStr(info["HEIGHT"])
        player_info["weight"] = info["WEIGHT"]
        player_info["country"] = info["COUNTRY"]
        player_info["jersey"] = info["JERSEY"]
        player_info["pos"] = info["POSITION"]
        player_info["team"] = info["TEAM_NAME"]

    # print(player_info)
    return player_info

def modifyStr(string):
    modstr = string.replace("-", " ft ")
    return modstr

def formatDate(date):
    bday_str = date
    bday_obj = datetime.strptime(bday_str, "%Y-%m-%dT%H:%M:%S")
    
    formatted_bday = bday_obj.strftime("%B %d, %Y")
    # print(formatted_bday)
    return formatted_bday

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
# data = list_players()
# print(data)
# get_players_full_name("lebron james")
# get_playerID("lebron james")
# get_players_by_first_name("john")   
# get_players_by_last_name("james")    


