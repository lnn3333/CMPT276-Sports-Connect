import json
from nba_api.stats.endpoints import teamgamelog
from teamProfileNBA import get_teamID

stats_dict = {
    "GAME_DATE" : None,
    "MATCHUP" : None,
    "WL" : None,
    "W" : None,
    "L" : None,
    "W_PCT" : None,
    "MIN" : None,
    "FGM" : None,
    "FGA" : None,
    "FG_PCT" : None,
    "FG3M" : None,
    "FG3A" : None,
    "FG3_PCT" : None,
    "FTM" : None,
    "FTA" : None,
    "FT_PCT" : None,
    "OREB" : None,
    "DREB" : None,
    "REB" : None,
    "AST" : None,
    "STL" : None,
    "BLK" : None,
    "TOV" : None,
    "PF" : None,
    "PTS" : None
}

teamID = get_teamID("Atlanta Hawks")
gamelog = teamgamelog.TeamGameLog(team_id=teamID)

gamelogjson = gamelog.get_normalized_json()
jsonobj = json.loads(gamelogjson)

# writing list of players to JSON file
with open("teamStatsNBA.json", "w") as file:
    json.dump(jsonobj, file, indent=4)

with open("teamStatsNBA.json", "r") as reading:
    data = json.load(reading)

# print(data)

# returns a list of matches for chosen team
def list_matches():
    
    match_list = []
    for match in data["TeamGameLog"]:
        
        match_list.append(match["MATCHUP"])
        sep = "\n"
        matches = sep.join(match_list)

    # print(match)
    return matches

# retrieves gameID given match
def get_gameID_by_match(match):
    match_count = 0
    match_dict = {}
    for gID in data["TeamGameLog"]:
        if match == gID["MATCHUP"]:
            match_count += 1
            gameID = gID["Game_ID"]
            match_dict[str(match_count)] = (gID["MATCHUP"], gID["GAME_DATE"], gID["Game_ID"])

    if match_count > 1:
        
        for key, tuple in match_dict.items():
            print(f"{key}: {' '.join(map(str, tuple[0:1]))}")
    
        chosenDate = input("Please choose a game date: ")
        if chosenDate in match_dict:
            gameID = match_dict[chosenDate][2]
            # print(gameID)
    
    return gameID
    

# function calls
m = list_matches()
print(m)
g = get_gameID_by_match("ATL @ DET")
print(g)