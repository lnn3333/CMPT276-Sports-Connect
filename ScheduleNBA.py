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

# formated terminal output for date and time 
def FormatDateTime(time):
    dateTime =datetime.strptime(time,"%Y-%m-%dT%H:%M:%SZ")
    formattedTime = dateTime.strftime("%I:%M:%S %p")
    formattedDate = dateTime.date()
    return formattedDate,formattedTime
 
#finds games based off user input of an alias   
def FindGamesForTeam(teamName,games):
    for game in games['games']:
        homeTeamAlias = game['home']['alias']
        awayTeamAlias = game['away']['alias']
        
        if homeTeamAlias == teamName:
            date,time=FormatDateTime(game['scheduled'])
            print(f"{date} - {game['home']['name']} vs {game['away']['name']} at {time}")
        elif awayTeamAlias == teamName:
            date,time=FormatDateTime(game['scheduled'])
            print(f"{date} - {game['away']['name']} vs {game['home']['name']} at {time}")

#testing
teamName = input("Please search for a team by their alias.(e.g, LAL for Los Angeles Lakers): ").upper()
FindGamesForTeam(teamName,games)

