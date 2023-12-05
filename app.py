from flask import Flask, render_template, request, redirect, url_for
from json.decoder import JSONDecodeError
from AwardRacesNBA import getCategories, readData, scoringChampRace, assistChampRace, ReboundChampRace, BlockChampRace, StealsChampRace 
from ScheduleNBA import getAllNBATeams,FindGamesForTeam, searchTeam, FormatDateTime, readData2,getImage
from news_api import readNews, getNews

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

@app.route('/team-schedule')
def teamSchedule():
    games = readData2()
    listOfTeams = getAllNBATeams(games)
    searchResult = request.args.get('searchResult')
    
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


@app.route('/pastSeason')
def pastSeason():
    return render_template('pastSeason.html')


if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0')