import http.client
import json

from datetime import datetime

#Below was done with the help of the SportsRadar API documentation
url = "/nba/trial/v8/en/games/2023/REG/schedule.json?api_key=2595gy5scfm5sgje8fa4de36"

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
with open("NBAGames.json","r") as reading:
    games = json.load(reading)

teamNames =set()

# formated terminal output for date and time 
def FormatDateTime(time):
    dateTime =datetime.strptime(time,"%Y-%m-%dT%H:%M:%SZ")
    formattedTime = dateTime.strftime("%I:%M:%S %p")
    formattedDate = dateTime.date()
    return formattedDate,formattedTime
 
#finds games based off user input of an alias   
def FindGamesForTeam(teamName,games):
    if teamName is None:
        print("Error: No team found")
        return
    else:
        for game in games['games']:
            homeTeamAlias = game['home']['alias']
            awayTeamAlias = game['away']['alias']
            #if Team is found print out the date and time of game
            if homeTeamAlias == teamName:
                date,time=FormatDateTime(game['scheduled'])
                print(f"{date} - {game['home']['name']} vs {game['away']['name']} at {time}")
            elif awayTeamAlias == teamName:
                date,time=FormatDateTime(game['scheduled'])
                print(f"{date} - {game['away']['name']} vs {game['home']['name']} at {time}")

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
def searchTeam(input):
    #Captialize the first letter of the word 
    formattedTeam=input.title()
    listOfTeams = getAllNBATeams(games)
    #return team's Alias
    for team in listOfTeams:
        if formattedTeam in team[1]:
            print("Found")
            return team[0]
    return None

inp =input("Enter team name:")
FindGamesForTeam(searchTeam(inp),games)