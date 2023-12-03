from flask import Flask, render_template, request, redirect, url_for
from AwardRacesNBA import getCategories, readData, scoringChampRace, assistChampRace, ReboundChampRace, BlockChampRace, StealsChampRace 
from ScheduleNBA import getAllNBATeams,FindGamesForTeam, searchTeam, FormatDateTime, readData2,getImage
from news_api import readNews, getNews
from playerCareerStatsNBA import readDataStats, get_available_reg_seasonID, regular_season_stats, post_season_stats, allstar_season_stats
from playerProfileNBA import list_players, readDataPlayer, get_players_full_name, get_playerID
from teamProfileNBA import get_teamID, get_team_info_by_nickname, get_team_info_by_abbr, get_team_info_by_state
from teamStatisticsNBA import readTeamData, get_teams, get_teamData, list_matches, get_team_stats

app = Flask(__name__)

#Home page
@app.route('/')
def home():
    news = readNews()
    listOfArticles = getNews(news)
    return render_template('index.html',listOfArticles=listOfArticles)

#route for award races 
@app.route('/nbaAwards', methods=['GET', 'POST'])
def displayAwardRace():
    if request.method == 'POST':
        print(request.form)
        chosenCat = request.form.get("statCategory")    
        data=readData()
        Points,Assist,Rebound,Blocks,Steals = getCategories(data)
        if chosenCat =='points':
            scoringChampRace(Points)
        elif chosenCat == 'assists':
            assistChampRace(Assist)
        elif chosenCat == 'rebounds':
            ReboundChampRace(Rebound)
        elif chosenCat == 'blocks':
            BlockChampRace(Blocks)
        elif chosenCat == 'steals':
            StealsChampRace(Steals)        

        return render_template('nbaAwards.html', chosenCat=chosenCat,Points=Points,Assist=Assist,Rebound=Rebound,Blocks=Blocks,Steals=Steals)

   
    return render_template('nbaAwards.html', chosenCat=None,Points=None,Assist=None,Rebound=None,Blocks=None,Steals=None)


# Add a route for schedule of recent games     
@app.route('/schedule')  
def schedule():
    return render_template('schedule.html')

@app.route('/team')  
def teamList():
    return render_template('team.html')

# @app.route('/team-schedule')
# def teamSchedule():
#     games = readData2()
#     listOfTeams = getAllNBATeams(games)
#     searchResult = request.args.get('searchResult')
    
    if searchResult:
        Team = searchTeam(searchResult,games)
        teamGames = FindGamesForTeam(Team,games)
        if teamGames is not None:
            teamImageList = {
                game['homeTeamName']: getImage(game['homeTeamName'])
                for game in teamGames
            }
        else:
            teamImageList = {"../static/assets/image/icons8-basketball-64.png"}

        return render_template('team-schedule.html',searchResult=searchResult,Team=Team,teamGames=teamGames,teamImagePaths=teamImageList)   
    return render_template('team-schedule.html',searchResult=None, team=None,teamGames=None,teamImagePaths=None)

@app.route('/player-profile')
def playerProfile():
    # pProfileData = readDataPlayer()
    # datastats = readDataStats()
    listOfPlayers = list_players()
        
    searchResult = request.args.get('searchResult')
    if searchResult:
        plr_name = get_players_full_name(searchResult)
        return render_template('player-profile.html', listOfPlayers=listOfPlayers, searchResult=searchResult, plr_name=plr_name)
    return render_template('player-profile.html', listOfPlayers=listOfPlayers, searchResult=None, plr_name=None)

@app.route('/team-profile')
def teamProfile():
    searchResult =  request.args.get('searchResult')
    # teamNickname, teamAbbr, teamState = None
    
    if searchResult:
        
        teamNickname = get_team_info_by_nickname(searchResult)
        if teamNickname:
            return render_template('team-profile.html', searchResult=searchResult, 
                                                        teamNickname=teamNickname, 
                                                        teamAbbr=None)
        else:
            teamAbbr = get_team_info_by_abbr(searchResult)
            if teamAbbr:
                return render_template('team-profile.html', searchResult=searchResult, 
                                                            teamNickname=None, 
                                                            teamAbbr=teamAbbr)
    return render_template('team-profile.html', searchResult=None, teamNickname=None, teamAbbr=None)

@app.route('/pastSeason')
def pastSeason():
    return render_template('pastSeason.html')

@app.route('/player-statistics', methods=['GET'])
def playerStats():
    data = readDataStats()
    regular_season = get_available_reg_seasonID(data)
    return render_template('player-statistics.html', regular_season=regular_season)

@app.route('/selectedSeason', methods=['POST'])
def selectedSeason():
    searchResult_stat = request.form.get('searchResult_stat')

    selected_season_id = request.form.get('selectedSeason')
    selected_season_type = request.form.get('selectedSeasonType')
    plr_id = get_playerID(searchResult_stat)
    selected_season = {'id': selected_season_id, 'type': selected_season_type}
    
    stats = None
    
    if selected_season_type == 'regular':
        stats = regular_season_stats(plr_id, selected_season_id)

    elif selected_season_type == "post":
        stats = post_season_stats(plr_id, selected_season_id)
    elif selected_season_type == "allstar":
        stats = allstar_season_stats(plr_id, selected_season_id)
        
    data = readDataStats()
    regular_season = get_available_reg_seasonID(data)
    
    return render_template('player-statistics.html', searchResult_stat=searchResult_stat, selected_season=selected_season, stats=stats, plr_id=plr_id, regular_season=regular_season)

@app.route('/team-statistics', methods=['GET'])
def teamStats():
    
    data = readTeamData()
    # from the form get the teamID (search), list the available matches (get gameID)
    teams_list = get_teams()
    return render_template('team-statistics.html', teams_list=teams_list)

@app.route('/selectedTeam', methods=["POST"])
def selectedTeam():
    
    selectedTeam = request.form.get('selectedTeam')
    team_id = get_teamID(selectedTeam)
    
    teams_list = get_teams()
    
    matches = list_matches(team_id)
    team_stats_list = []
    
    for _, gameid in matches:
        team_stats = get_team_stats(gameid)
        team_stats_list.append(team_stats)
        
    combined_data = zip(matches, team_stats_list)
    
    return render_template('team-statistics.html', selectedTeam=selectedTeam, team_id=team_id, matches=matches, combined_data=combined_data, teams_list=teams_list)

if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0')