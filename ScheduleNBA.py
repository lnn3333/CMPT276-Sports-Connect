import http.client
import json

from datetime import datetime
import pytz

#Below was done with the help of the SportsRadar API documentation
url = "/nba/trial/v8/en/games/2023/REG/schedule.json?api_key=26s9kjdgbgmtakysh5t9c9zu"

conn = http.client.HTTPSConnection("api.sportradar.us")
conn.request("GET", url)

response = conn.getresponse()
data = response.read()

decodedData=data.decode("utf-8")
conn.close()

GamesJSON = json.loads(decodedData)

#store JSON data
with open ("NBAGames.json","w") as file:
    json.dump(GamesJSON,file,indent=4)

#read JSON data
def readData2():
    with open("NBAGames.json","r") as reading:
        games = json.load(reading)
    return games

teamNames =set()

# formated terminal output for date and time 
def FormatDateTime(time):
    dateTime =datetime.strptime(time,"%Y-%m-%dT%H:%M:%SZ")
    
    gmtTime=pytz.timezone('GMT')
    pstTime=pytz.timezone('America/Los_Angeles')
    
    localTime = gmtTime.localize(dateTime)
    pstLocalTime=localTime.astimezone(pstTime)
    

    formattedTime = pstLocalTime.strftime("%I:%M:%S %p")
    formattedDate = pstLocalTime.date()
    return formattedDate,formattedTime
 
#finds games based off user input of an alias   
def FindGamesForTeam(teamName,games):
    if teamName is None:
        print("Error: No team found")
        return
    else:
        teamGames=[]
        for game in games['games']:
            homeTeamAlias = game['home']['alias']
            awayTeamAlias = game['away']['alias']
            #if Team is found print out the date and time of game
            if homeTeamAlias == teamName:
                date,time=FormatDateTime(game['scheduled'])
                homeTeamName = game['home']['name']
                awayTeamName = game['away']['name']
                teamGames.append({'date':date,'time':time,'homeTeamName':homeTeamName,'awayTeamName':awayTeamName,'homeTeamAlias':homeTeamAlias,'awayTeamAlias':awayTeamAlias})
            elif awayTeamAlias == teamName:
                date,time=FormatDateTime(game['scheduled'])
                homeTeamName = game['home']['name']
                awayTeamName = game['away']['name']
                teamGames.append({'date':date,'time':time,'homeTeamName':homeTeamName,'awayTeamName':awayTeamName,'homeTeamAlias':homeTeamAlias,'awayTeamAlias':awayTeamAlias})
    return teamGames
                
                

#get the list of NBATeams 
def getAllNBATeams(games):
    for game in games['games']:
        
        homeTeamAlias = game['home']['alias']
        homeTeamName = game['home']['name']
        
        awayTeamAlias = game['away']['alias']
        awayTeamName =game['away']['name']
        
        #Add Team Name and Alias as a tuple in the List
        if homeTeamAlias and homeTeamName:
            teamNames.add((homeTeamAlias,homeTeamName))
        
        if awayTeamAlias and awayTeamName:
            teamNames.add((awayTeamAlias,awayTeamName))
    #Return a sorted list
    listOfTeams = sorted(list(teamNames))
    return listOfTeams

#Search team name, Full or partial 
def searchTeam(input,games):
    #Captialize the first letter of the word 
    formattedTeam=input.title()
    listOfTeams = getAllNBATeams(games)
    #return team's Alias
    for team in listOfTeams:
        if formattedTeam in team[1]:
            #print("Found")
            return team[0]
    return None

#inp =input("Enter team name:")
#FindGamesForTeam(searchTeam(inp),games)
teamImageMap = {
'Boston Celtics' : "../static/assets/image/boston-celtics.png",
'Brooklyn Nets' : "../static/assets/image/brooklyn-nets.png",
'New York Knicks': "../static/assets/image/new_york_knicks.png",
'Philadelphia 76ers' :"../static/assets/image/philadelphia_76.png",
'Toronto Raptors':"../static/assets/image/raptors.png",

'Chicago Bulls' : "../static/assets/image/chicago-bulls.png",
'Cleveland Cavaliers': "../static/assets/image/cleveland-cavaliers.png",
'Detroit Pistons': "../static/assets/image/detroit-pistons.png",
'Indiana Pacers' : "../static/assets/image/indiana-pacers.png",
'Milwaukee Bucks': "../static/assets/image/milwaukee-bucks.png",

'Atlanta Hawks': "../static/assets/image/atlanta-hawks.png",
'Charlotte Hornets': "../static/assets/image/charlotte-hornets.png",
'Miami Heat': "../static/assets/image/miami-heat.png",
'Orlando Magic': "../static/assets/image/orlando-magic.png",
'Washington Wizards': "../static/assets/image/washington-wizards.png",

'Denver Nuggets': "../static/assets/image/denver-nuggets.png",
'Minnesota Timberwolves': "../static/assets/image/minnesota-timberwolves.png",
'Oklahoma City Thunder': "../static/assets/image/oklahoma-city-thunder.png",
'Portland Trail Blazers': "../static/assets/image/portland-trail-blazers.png",
'Utah Jazz': "../static/assets/image/utah-jazz-vector.png",

'Golden State Warriors': "../static/assets/image/golden-state-warriorsr.png",
'LA Clippers': "../static/assets/image/los-angeles-clippers.png",
'Los Angeles Lakers': "../static/assets/image/los_angeles_lakers.png",
'Phoenix Suns': "../static/assets/image/phoenix-suns.png",
'Sacramento Kings': "../static/assets/image/sacramento-kings-logo.png",

'Dallas Mavericks': "../static/assets/image/dallas-mavericks.png",
'Houston Rockets': "../static/assets/image/houston-rockets.png",
'Memphis Grizzlies': "../static/assets/image/memphis-grizzlies.png",
'New Orleans Pelicans': "../static/assets/image/new-orleans-pelicans.png",
'San Antonio Spurs': "../static/assets/image/SanAntonio.png",
}

def getImage(teamName):
    if teamName in teamImageMap:
        return teamImageMap[teamName]
    else:
        return "../static/assets/image/icons8-basketball-64.png"
        
