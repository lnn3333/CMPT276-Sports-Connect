import json
from nba_api.stats.static import teams

teamsNBA = teams.get_teams()

# writing list of players to JSON file
with open("teamsNBA.json", "w") as file:
    json.dump(teamsNBA, file, indent=4)

with open("teamsNBA.json", "r") as reading:
    data = json.load(reading)

# Retrieves teamID
def get_teamID(team):
    team = teams.find_teams_by_full_name(team)
    teamID = team[0]["id"]
    print(teamID)

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
# get_teamID("Atlanta Hawks")