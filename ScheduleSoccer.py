import http.client
import json

from datetime import datetime

#Below was done with the help of the SportsRadar API documentation
url = "/soccer/trial/v4/en/seasons/sr:season:105353/schedules.json?api_key=a9wpvfq5favxzvxe4w9dj74m"

conn = http.client.HTTPSConnection("api.sportradar.us")
conn.request("GET", url)

response = conn.getresponse()
data = response.read()

decodedData=data.decode("utf-8")
conn.close()

GamesJSON = json.loads(decodedData)

#store JSON data
with open ("SoccerGames.json","w") as file:
    json.dump(GamesJSON,file,indent=4)
    
#read JSON data
with open("SoccerGames.json","r") as reading:
    soccerGames = json.load(reading)
    
teams = set()

# formated terminal output for date and time 
def FormatDateTime(time):
    dateTime =datetime.strptime(time,"%Y-%m-%dT%H:%M:%S%z")
    formattedTime = dateTime.strftime("%I:%M:%S %p")
    formattedDate = dateTime.date()
    return formattedDate,formattedTime

def getAllTeams():
    for game in soccerGames['schedules']:
        
        homeTeam = game['sport_event']['competitors'][0]['name']
        awayTeam = game['sport_event']['competitors'][1]['name']
        
        if homeTeam:
            teams.add(homeTeam)
        if awayTeam:
            teams.add(awayTeam)
            
    listOfTeams = sorted(list(teams))
    return listOfTeams

def searchTeam(input):
    #format input to match case
    formatInput = input.title()
    listOfTeams = getAllTeams()
    #find the team name 
    for team in listOfTeams:
        if formatInput in team.title():
            return team
    return None

def FindTeamGames(team):
    if team is not None:
     for game in soccerGames['schedules']:
        
        homeTeam = game['sport_event']['competitors'][0]['name']
        awayTeam = game['sport_event']['competitors'][1]['name']
        
        if team == homeTeam:
            date,time = FormatDateTime(game['sport_event']['start_time'])
            print(f"{date} - {homeTeam}(H) vs {awayTeam}(A) at {time}")
       
        elif team == awayTeam:
            date,time = FormatDateTime(game['sport_event']['start_time'])
            print(f"{date} - {awayTeam}(A) vs {homeTeam}(H) at {time}")
    else:
        print("Cannot Find Team")

inp=input("Enter Team name:")
FindTeamGames(searchTeam(inp))


