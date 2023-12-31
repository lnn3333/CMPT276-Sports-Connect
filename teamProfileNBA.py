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
    # print(dataInfo)

# Retrieves teamID
def get_teamID(team):
    team = teams.find_teams_by_full_name(team)
    teamID = team[0]["id"]
    # print(teamID)
    return teamID

# lists seasonID
def list_seasonID():
    seasons = []
    for sID in dataInfo["AvailableSeasons"]:
        seasons.append(sID["SEASON_ID"])
        sep = "\n"
        available_seasons = sep.join(seasons)
        # print(available_seasons)
    return available_seasons

# retrieves team info by state
def get_team_info_by_state(state):
    
    teamState = teams.find_teams_by_state(state)
    
    teamState_count = 0
    teamState_dict = {}
    
    for ts in data:
        if ts["state"] == state:
        # if teamState[teamState_count]["state"] == ts["state"]:
            teamState_count += 1
            teamState_dict[str(teamState_count)] = (ts["id"], ts["full_name"])
            
    if teamState_count > 1:
        
        for key, tuple in teamState_dict.items():
            print(f"{key}: {tuple[1]}")
            
        chosenState = input("\nPlease choose a team: ")
        if chosenState in teamState_dict:
            teamID = get_teamID(teamState_dict[chosenState][1])
            return get_team_info(teamID=teamID)
    else:
        teamID = get_teamID(teamState[0]["full_name"])
        return get_team_info(teamID=teamID)
        
# retrieves team info by abbreviation
def get_team_info_by_abbr(abbr):
    
    teamAbbr = teams.find_team_by_abbreviation(abbr)
    if teamAbbr:
        return get_team_info(teamAbbr["id"])
    return None
    
# retrieves team info by city
def get_team_info_by_city(city):
    
    teamCity = teams.find_teams_by_city(city)
    # print(teamCity)
    
    teamCity_count = 0
    teamCity_dict = {}
    
    for tc in data:
        if teamCity[teamCity_count-1]["full_name"] == tc["full_name"]:
            teamCity_count += 1
            print(teamCity_count)
            teamCity_dict[str(teamCity_count)] = (tc["id"], tc["full_name"])

    if teamCity_count > 1:
        
        for key, tuple in teamCity_dict.items():
            print(f"{key}: {tuple[1]}")
            
        chosenCity = input("\nPlease choose a team: ")
        if chosenCity in teamCity_dict:
            teamID = get_teamID(teamCity_dict[chosenCity][1])
            return get_team_info(teamID=teamID)
    # else:
    #     teamID = get_teamID(teamCity[0]["full_name"])
    #     get_team_info(teamID=teamID)
    
# retrieves team info by nickname
def get_team_info_by_nickname(nickname):
    
    teamNick =  teams.find_teams_by_nickname(nickname)
    if teamNick:
        return get_team_info(teamNick[0]["id"])
    return None

# retrieves team info
def get_team_info(teamID):
    
    teamProfile = teaminfocommon.TeamInfoCommon(team_id=teamID)
    tf = teamProfile.get_normalized_json()
    
    jsonobj = json.loads(tf)
    
    team_info = {}
    for info in jsonobj["TeamInfoCommon"]:
        
        team_info['szn_year'] = info["SEASON_YEAR"]
        team_info['tCity'] = info["TEAM_CITY"]
        team_info['tName'] = info["TEAM_NAME"]
        team_info['tAbbr'] = info["TEAM_ABBREVIATION"]
        team_info['tConf'] = info["TEAM_CONFERENCE"]
        team_info['tDiv'] = info["TEAM_DIVISION"]
        team_info['tW'] = str(info["W"])
        team_info['tL'] = str(info["L"])
        team_info['pct']= str(info["PCT"])
        team_info['conf_rank'] = str(info["CONF_RANK"])
        team_info['div_rank'] = str(info["DIV_RANK"])
    
    # print(team_info)  
    return team_info
    # display_team_profile(szn_year, tCity, tName, tAbbr, tConf, tDiv, tW, tL, pct, conf_rank, div_rank)

# lists all the teams in NBAA
def list_teams():
    teamsNBA = []
    for teams in data:
        teamsNBA.append(teams["full_name"])
        sep = "\n"
        list = sep.join(teamsNBA)
        
    print(list)

# displays team profile info
def display_team_profile(sznyear, city, name, abbr, conf, div, w, l, pct, cR, dR):
    pf_arr = []
    
    pf_arr.append(sznyear)
    pf_arr.append(city)
    pf_arr.append(name)
    pf_arr.append(abbr)
    pf_arr.append(conf)
    pf_arr.append(div)
    pf_arr.append(w)
    pf_arr.append(l)
    pf_arr.append(pct)
    pf_arr.append(cR)
    pf_arr.append(dR)
    
    sep = "\n"
    display = sep.join(pf_arr)
    print(display)
    
# function calls
# list_teams()
# t = get_teamID("Atlanta Hawks")
# print(t)
# list_seasonID()
# get_team_info(t)
# get_team_info_by_state("Atlanta")
# get_team_info_by_abbr("cle")
# get_team_info_by_city("los angeles")
# get_team_info_by_nickname("Rockets")
 