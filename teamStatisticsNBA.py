import json
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams
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

# teamID = get_teamID("Atlanta Hawks")
# gamelog = teamgamelog.TeamGameLog(team_id=teamID)

# gamelogjson = gamelog.get_normalized_json()
# jsonobj = json.loads(gamelogjson)

# # writing list of players to JSON file
# with open("teamStatsNBA.json", "w") as file:
#     json.dump(jsonobj, file, indent=4)

# with open("teamStatsNBA.json", "r") as reading:
#     data = json.load(reading)

# print(data)

def get_teamData(teamID):
    gamelog = teamgamelog.TeamGameLog(team_id=teamID)

    gamelogjson = gamelog.get_normalized_json()
    jsonobj = json.loads(gamelogjson)

    # writing list of players to JSON file
    with open("teamStatsNBA.json", "w") as file:
        json.dump(jsonobj, file, indent=4)

    with open("teamStatsNBA.json", "r") as reading:
        data = json.load(reading)
    
    return data

def readTeamData():
    with open("teamStatsNBA.json", "r") as reading:
        data = json.load(reading)
    
    return data

def get_teams():
    all_teams = teams.get_teams()
    team_names = []
    for info in all_teams:
        team_names.append(info["full_name"])
    return team_names

# returns a list of matches for chosen team
def list_matches(teamID):
    
    data = get_teamData(teamID)
    
    match_list = []
    for match in data["TeamGameLog"]:
        
        match_tup = (match["MATCHUP"], match["Game_ID"])
        match_list.append(match_tup)
        # sep = "\n"
        # matches = sep.join(match_list)

    # print(match)
    return match_list

# retrieves gameID given match
def get_gameID_by_match(match):
    
    data = readTeamData()
    
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
    
    data = readTeamData()

    for stats in data["TeamGameLog"]:
        if gameID == stats["Game_ID"]:
            stats_dict = {
                "GAME_DATE": stats["GAME_DATE"],
                "MATCHUP": stats["MATCHUP"],
                "WL": stats["WL"],
                "W": stats["W"],
                "L": stats["L"],
                "W_PCT": stats["W_PCT"],
                "MIN": stats["MIN"],
                "FGM": stats["FGM"],
                "FGA": stats["FGA"],
                "FG_PCT": stats["FG_PCT"],
                "FG3M": stats["FG3M"],
                "FG3A": stats["FG3A"],
                "FG3_PCT": stats["FG3_PCT"],
                "FTM": stats["FTM"],
                "FTA": stats["FTA"],
                "FT_PCT": stats["FT_PCT"],
                "OREB": stats["OREB"],
                "DREB": stats["DREB"],
                "REB": stats["REB"],
                "AST": stats["AST"],
                "STL": stats["STL"],
                "BLK": stats["BLK"],
                "TOV": stats["TOV"],
                "PF": stats["PF"],
                "PTS": stats["PTS"]
            }
            
            return stats_dict
    return {}
            
def display_stats(dict):
    for key, value in dict.items():
        print(key, ":", value)
        
# function calls
# list_matches()
# g = get_gameID_by_match("ATL @ DET")
# get_team_stats(g)
# display_stats(stats_dict)
# get_teams()