import json
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teaminfocommon

teamsNBA = teams.get_teams()
teamInfoNBA = teaminfocommon.TeamInfoCommon(team_id=1610612737)

# writing list of players to JSON file
with open("teamsNBA.json", "w") as file:
    json.dump(teamsNBA, file, indent=4)

with open("teamsNBA.json", "r") as reading:
    data = json.load(reading)

teamInfojson = teamInfoNBA.get_normalized_json()
jsonobj = json.loads(teamInfojson)

with open("teamsInfoNBA.json", "w") as file:
    json.dump(jsonobj, file, indent=4)

with open("teamsInfoNBA.json", "r") as reading:
    dataInfo = json.load(reading)
    print(dataInfo)

# Retrieves teamID
def get_teamID(team):
    team = teams.find_teams_by_full_name(team)
    teamID = team[0]["id"]
    # print(teamID)
    return teamID

# Retrieves seasonID
def list_seasonID():
    seasons = []
    for sID in dataInfo["AvailableSeasons"]:
        seasons.append(sID["SEASON_ID"])
        sep = "\n"
        available_seasons = sep.join(seasons)
        # print(available_seasons)
    return available_seasons
            
# def get_team_info(teamID):
    

# lists all the teams in NBAA
def list_teams():
    teamsNBA = []
    for teams in data:
        teamsNBA.append(teams["full_name"])
        sep = "\n"
        list = sep.join(teamsNBA)
        
    print(list)
    
# function calls
# list_teams()
# t = get_teamID("Atlanta Hawks")
# print(t)
# list_seasonID()