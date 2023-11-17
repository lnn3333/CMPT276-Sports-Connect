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

# retrieves team game stats from a particular match
def get_team_stats(gameID):

    for stats in data["TeamGameLog"]:
        if gameID == stats["Game_ID"]:
            stats_dict["GAME_DATE"] = stats["GAME_DATE"]
            stats_dict["MATCHUP"] = stats["MATCHUP"]
            stats_dict["WL"] = stats["WL"]
            stats_dict["W"] = stats["W"]
            stats_dict["L"] = stats["L"]
            stats_dict["W_PCT"] = stats["W_PCT"]
            stats_dict["MIN"] = stats["MIN"]
            stats_dict["FGM"] = stats["FGM"]
            stats_dict["FGA"] = stats["FGA"]
            stats_dict["FG_PCT"] = stats["FG_PCT"]
            stats_dict["FG3M"] = stats["FG3M"]
            stats_dict["FG3A"] = stats["FG3A"]
            stats_dict["FG3_PCT"] = stats["FG3_PCT"]
            stats_dict["FTM"] = stats["FTM"]
            stats_dict["FTA"] = stats["FTA"]
            stats_dict["FT_PCT"] = stats["FT_PCT"]
            stats_dict["OREB"] = stats["OREB"]
            stats_dict["DREB"] = stats["DREB"]
            stats_dict["REB"] = stats["REB"]
            stats_dict["AST"] = stats["AST"]
            stats_dict["STL"] = stats["STL"]
            stats_dict["BLK"] = stats["BLK"]
            stats_dict["TOV"] = stats["TOV"]
            stats_dict["PF"] = stats["PF"]
            stats_dict["PTS"] = stats["PTS"]
            
def display_stats(dict):
    for key, value in dict.items():
        print(key, ":", value)
        
# function calls
# list_matches()
g = get_gameID_by_match("ATL @ DET")
get_team_stats(g)
display_stats(stats_dict)