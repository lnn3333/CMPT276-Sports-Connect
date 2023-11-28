from flask import Flask, render_template, request
from AwardRacesNBA import getCategories, readData, scoringChampRace, assistChampRace, ReboundChampRace, BlockChampRace, StealsChampRace 
from ScheduleNBA import getAllNBATeams,FindGamesForTeam, searchTeam, FormatDateTime, readData2,getImage
from news_api import readNews, getNews
from playerCareerStatsNBA import readDataStats, get_available_reg_seasonID, regular_season_stats
from playerProfileNBA import list_players, readDataPlayer, get_players_full_name
from teamProfileNBA import get_team_info_by_nickname, get_team_info_by_abbr, get_team_info_by_state

app = Flask(__name__)

#Home page
@app.route('/')
def home():
    news = readNews()
    listOfArticles = getNews(news)
    return render_template('index.html',listOfArticles=listOfArticles)

#route for award races 
@app.route('/nbaAwards')
def displayAwardRace():
    data=readData()
    Points,Assist,Rebound,Blocks,Steals = getCategories(data)
    scoringChampRace(Points)
    assistChampRace(Assist)
    ReboundChampRace(Rebound)
    BlockChampRace(Blocks)
    StealsChampRace(Steals)
   
    return render_template('nbaAwards.html',
                           Points=Points,
                           Assist=Assist,
                           Rebound=Rebound,
                           Blocks=Blocks,
                           Steals=Steals)

# Add a route for schedule of recent games     
@app.route('/schedule')  
def schedule():
    return render_template('schedule.html')

@app.route('/team')  
def teamList():
    return render_template('team.html')

@app.route('/team-schedule')
def teamSchedule():
    games = readData2()
    listOfTeams = getAllNBATeams(games)
    searchResult = request.args.get('searchResult')
    
    if searchResult:
        Team = searchTeam(searchResult,games)
        teamGames = FindGamesForTeam(Team,games)
        teamImageList ={
            game['homeTeamName']:getImage(game['homeTeamName'])
            for game in teamGames
        }
        return render_template('team-schedule.html',searchResult=searchResult,Team=Team,teamGames=teamGames,teamImagePaths=teamImageList)   
    return render_template('team-schedule.html',searchResult=None, team=None,teamGames=None,teamImagePaths={})

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

if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0')