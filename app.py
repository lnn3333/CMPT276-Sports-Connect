from flask import Flask, render_template, request
from AwardRacesNBA import getCategories, readData, scoringChampRace, assistChampRace, ReboundChampRace, BlockChampRace, StealsChampRace 
from ScheduleNBA import getAllNBATeams,FindGamesForTeam, searchTeam, FormatDateTime, readData2,getImage

app = Flask(__name__)

#Home page
@app.route('/')
def home():
    return render_template('index.html')

#route for award races 
@app.route('/nbaAwards.html')
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
@app.route('/schedule.html')  
def schedule():
    return render_template('schedule.html')

@app.route('/team.html')  
def teamList():
    return render_template('team.html')

@app.route('/team-schedule.html')
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

@app.route('/news.html')
def news():
    return render_template('news.html')


if __name__== '__main__':
    app.run(debug=True)