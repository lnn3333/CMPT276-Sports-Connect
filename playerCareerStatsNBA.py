import json
import numpy as np
from nba_api.stats.endpoints import playercareerstats

from playerProfileNBA import get_playerID
from playerProfileNBA import get_players_full_name

npArr = []

stats_dict = {
    'gp' : None,
    'gs' : None,
    'mins' : None,
    'fgm' : None,
    'fga' : None,
    'fg_pct' : None,
    'fg3m' : None,
    'fg3a' : None,
    'fg3_pct' : None,
    'ftm' : None,
    'fta' : None,
    'ft_pct' : None,
    'oreb' : None,
    'dreb' : None,
    'reb' : None,
    'ast' : None,
    'stl' : None,
    'blk' : None,
    'tov' : None,
    'pf' : None,
    'pts' : None
}

# player_name = get_players_full_name("lebron james")
playerID = get_playerID("lebron james")

# valid_url = "https://stats.nba.com/stats/playercareerstats?LeagueID=&PerMode=" 
# + perMode_Totals + "&PlayerID=" + playerID

career = playercareerstats.PlayerCareerStats(player_id=playerID)

careerjson = career.get_normalized_json()
jsonobj = json.loads(careerjson)

# writing player info to JSON file
with open("playerStatsNBA.json", "w") as file:
    json.dump(jsonobj, file, indent=4)

with open("playerStatsNBA.json", "r") as reading:
    datastats = json.load(reading)

#season/career->regular/post/allstar

def readDataStats():
    with open("playerStatsNBA.json", "r") as reading:
        datastats = json.load(reading)
    return datastats

def get_available_reg_seasonID(datastats):
    
    seasons = []
    
    for sID in datastats["SeasonTotalsRegularSeason"]:
        seasons.append(sID["SEASON_ID"])
        sep = "\n"
        available_seasons = sep.join(seasons)
    
    return available_seasons

def get_available_post_seasonID():
    
    seasons = []
    
    for sID in datastats["SeasonTotalsPostSeason"]:
        seasons.append(sID["SEASON_ID"])
        sep = "\n"
        available_seasons = sep.join(seasons)
    
    return available_seasons

def get_available_allstar_seasonID():
    
    seasons = []
    
    for sID in datastats["SeasonTotalsAllStarSeason"]:
        seasons.append(sID["SEASON_ID"])
        sep = "\n"
        available_seasons = sep.join(seasons)
    
    return available_seasons

def regular_season_stats(season):
    
    global npArr
    stats = []
    
    for data in datastats["SeasonTotalsRegularSeason"]:
        if season == data["SEASON_ID"]:
            stats_dict["gp"] = data["GP"]
            stats_dict["gs"] = data["GS"]
            stats_dict["mins"] = data["MIN"]
            stats_dict["fgm"] = data["FGM"]
            stats_dict["fga"] = data["FGA"]
            stats_dict["fg_pct"] = data["FG_PCT"]
            stats_dict["fg3m"] = data["FG3M"]
            stats_dict["fg3a"] = data["FG3A"]
            stats_dict["fg3_pct"] = data["FG3_PCT"]
            stats_dict["ftm"] = data["FTM"]
            stats_dict["fta"] = data["FTA"]
            stats_dict["ft_pct"] = data["FT_PCT"]
            stats_dict["oreb"] = data["OREB"]
            stats_dict["dreb"] = data["DREB"]
            stats_dict["reb"] = data["REB"]
            stats_dict["ast"] = data["AST"]
            stats_dict["stl"] = data["STL"]
            stats_dict["blk"] = data["BLK"]
            stats_dict["tov"] = data["TOV"]
            stats_dict["pf"] = data["PF"]
            stats_dict["pts"] = data["PTS"]
    
    # convert dictionary to array
    # res = stats_dict.items()
    # data_list = list(res)
    # npArr = np.array(data_list)
    
    # store data in array
    # stats = []
    # for data in npArr:
    #     stats.append(data[1])

    # print(stats_dict)
    
    return stats

def post_season_stats(season):
    
    for data in datastats["SeasonTotalsPostSeason"]:
        if season == data["SEASON_ID"]:
            stats_dict["gp"] = data["GP"]
            stats_dict["gs"] = data["GS"]
            stats_dict["mins"] = data["MIN"]
            stats_dict["fgm"] = data["FGM"]
            stats_dict["fga"] = data["FGA"]
            stats_dict["fg_pct"] = data["FG_PCT"]
            stats_dict["fg3m"] = data["FG3M"]
            stats_dict["fg3a"] = data["FG3A"]
            stats_dict["fg3_pct"] = data["FG3_PCT"]
            stats_dict["ftm"] = data["FTM"]
            stats_dict["fta"] = data["FTA"]
            stats_dict["ft_pct"] = data["FT_PCT"]
            stats_dict["oreb"] = data["OREB"]
            stats_dict["dreb"] = data["DREB"]
            stats_dict["reb"] = data["REB"]
            stats_dict["ast"] = data["AST"]
            stats_dict["stl"] = data["STL"]
            stats_dict["blk"] = data["BLK"]
            stats_dict["tov"] = data["TOV"]
            stats_dict["pf"] = data["PF"]
            stats_dict["pts"] = data["PTS"]
            
def allstar_season_stats(season):
    
    for data in datastats["SeasonTotalsAllStarSeason"]:
        if season == data["SEASON_ID"]:
            stats_dict["gp"] = data["GP"]
            stats_dict["gs"] = data["GS"]
            stats_dict["mins"] = data["MIN"]
            stats_dict["fgm"] = data["FGM"]
            stats_dict["fga"] = data["FGA"]
            stats_dict["fg_pct"] = data["FG_PCT"]
            stats_dict["fg3m"] = data["FG3M"]
            stats_dict["fg3a"] = data["FG3A"]
            stats_dict["fg3_pct"] = data["FG3_PCT"]
            stats_dict["ftm"] = data["FTM"]
            stats_dict["fta"] = data["FTA"]
            stats_dict["ft_pct"] = data["FT_PCT"]
            stats_dict["oreb"] = data["OREB"]
            stats_dict["dreb"] = data["DREB"]
            stats_dict["reb"] = data["REB"]
            stats_dict["ast"] = data["AST"]
            stats_dict["stl"] = data["STL"]
            stats_dict["blk"] = data["BLK"]
            stats_dict["tov"] = data["TOV"]
            stats_dict["pf"] = data["PF"]
            stats_dict["pts"] = data["PTS"]
    

def career_reg_season_stats():
    for data in datastats["CareerTotalsRegularSeason"]:
        stats_dict["gp"] = data["GP"]
        stats_dict["gs"] = data["GS"]
        stats_dict["mins"] = data["MIN"]
        stats_dict["fgm"] = data["FGM"]
        stats_dict["fga"] = data["FGA"]
        stats_dict["fg_pct"] = data["FG_PCT"]
        stats_dict["fg3m"] = data["FG3M"]
        stats_dict["fg3a"] = data["FG3A"]
        stats_dict["fg3_pct"] = data["FG3_PCT"]
        stats_dict["ftm"] = data["FTM"]
        stats_dict["fta"] = data["FTA"]
        stats_dict["ft_pct"] = data["FT_PCT"]
        stats_dict["oreb"] = data["OREB"]
        stats_dict["dreb"] = data["DREB"]
        stats_dict["reb"] = data["REB"]
        stats_dict["ast"] = data["AST"]
        stats_dict["stl"] = data["STL"]
        stats_dict["blk"] = data["BLK"]
        stats_dict["tov"] = data["TOV"]
        stats_dict["pf"] = data["PF"]
        stats_dict["pts"] = data["PTS"]
        
def career_post_season_stats():
    for data in datastats["CareerTotalsPostSeason"]:
        stats_dict["gp"] = data["GP"]
        stats_dict["gs"] = data["GS"]
        stats_dict["mins"] = data["MIN"]
        stats_dict["fgm"] = data["FGM"]
        stats_dict["fga"] = data["FGA"]
        stats_dict["fg_pct"] = data["FG_PCT"]
        stats_dict["fg3m"] = data["FG3M"]
        stats_dict["fg3a"] = data["FG3A"]
        stats_dict["fg3_pct"] = data["FG3_PCT"]
        stats_dict["ftm"] = data["FTM"]
        stats_dict["fta"] = data["FTA"]
        stats_dict["ft_pct"] = data["FT_PCT"]
        stats_dict["oreb"] = data["OREB"]
        stats_dict["dreb"] = data["DREB"]
        stats_dict["reb"] = data["REB"]
        stats_dict["ast"] = data["AST"]
        stats_dict["stl"] = data["STL"]
        stats_dict["blk"] = data["BLK"]
        stats_dict["tov"] = data["TOV"]
        stats_dict["pf"] = data["PF"]
        stats_dict["pts"] = data["PTS"]
        
def career_allstar_season_stats():
    for data in datastats["CareerTotalsAllStarSeason"]:
        stats_dict["gp"] = data["GP"]
        stats_dict["gs"] = data["GS"]
        stats_dict["mins"] = data["MIN"]
        stats_dict["fgm"] = data["FGM"]
        stats_dict["fga"] = data["FGA"]
        stats_dict["fg_pct"] = data["FG_PCT"]
        stats_dict["fg3m"] = data["FG3M"]
        stats_dict["fg3a"] = data["FG3A"]
        stats_dict["fg3_pct"] = data["FG3_PCT"]
        stats_dict["ftm"] = data["FTM"]
        stats_dict["fta"] = data["FTA"]
        stats_dict["ft_pct"] = data["FT_PCT"]
        stats_dict["oreb"] = data["OREB"]
        stats_dict["dreb"] = data["DREB"]
        stats_dict["reb"] = data["REB"]
        stats_dict["ast"] = data["AST"]
        stats_dict["stl"] = data["STL"]
        stats_dict["blk"] = data["BLK"]
        stats_dict["tov"] = data["TOV"]
        stats_dict["pf"] = data["PF"]
        stats_dict["pts"] = data["PTS"]

def display_stats(dict):
   
    for key, value in dict.items():
        print(key, ":", value)
    
            
            
# function calls
# regular_season_stats("2004-05")
career_reg_season_stats()
# post_season_stats("2005-06")
# career_post_season_stats()
# allstar_season_stats("2004-05")
# career_allstar_season_stats()
display_stats(stats_dict)

    