import http.client
import json

url = "/nba/trial/v8/en/seasons/2023/REG/leaders.json?api_key=2595gy5scfm5sgje8fa4de36"

conn = http.client.HTTPSConnection("api.sportradar.us")
conn.request("GET", url)

response = conn.getresponse()
data = response.read()

decodedData=data.decode("utf-8")
conn.close()

LeadersJSON = json.loads(decodedData)

with open ("leaders.json","w") as file:
    json.dump(LeadersJSON,file,indent=4)

with open("leaders.json","r") as reading:
    DataSc = json.load(reading)
   
for category in DataSc['categories']:
    if category['name'] == 'points' and category['type'] == 'average':
        pointsPerGame = category
    elif category['name'] == 'assists' and category['type'] == 'average':
        assistPerGame = category
    elif category['name'] == 'rebounds' and category['type'] == 'average':
        reboundsPerGame = category
    elif category['name'] == 'blocks' and category['type'] == 'average':
        blocksPerGame = category
    elif category['name'] == 'steals' and category['type'] == 'average':
        stealsPerGame = category

def scoringChampRace(pointsPerGame):
    if pointsPerGame is not None:
        ranks = pointsPerGame['ranks'][:10]
        print("Top 10:")
        for rank in ranks:
            print(rank['player']['full_name'],"--->",rank['score'])
    else:
        print("Category not found.")

def assistChampRace(assistPerGame):
    if assistPerGame is not None:
        ranks = assistPerGame['ranks'][:10]
        print("Top 10:")
        for rank in ranks:
            print(rank['player']['full_name'],"--->",rank['score'])
    else:
        print("Category not found.")

def ReboundChampRace(reboundsPerGame):
    if reboundsPerGame is not None:
        ranks = reboundsPerGame['ranks'][:10]
        print("Top 10:")
        for rank in ranks:
            print(rank['player']['full_name'],"--->",rank['score'])
    else:
        print("Category not found.")

def BlockChampRace(blocksPerGame):
    if blocksPerGame is not None:
        ranks = blocksPerGame['ranks'][:10]
        print("Top 10:")
        for rank in ranks:
            print(rank['player']['full_name'],"--->",rank['score'])
    else:
        print("Category not found.")

def StealsChampRace(stealsPerGame):
    if stealsPerGame is not None:
        ranks = stealsPerGame['ranks'][:10]
        print("Top 10:")
        for rank in ranks:
            print(rank['player']['full_name'],"--->",rank['score'])
    else:
        print("Category not found.")

on = True
while on:
    print("=========================================")
    choice=input("Please chose one of the following:\n 1.Scoring champ race\n 2. Assist champ race \n 3. Rebound champ race \n 4.Block champ race \n 5.Steal champ race\n")
    if choice=="1":
        scoringChampRace(pointsPerGame)
    elif choice=="2":
        assistChampRace(assistPerGame)
    elif choice=="3":
        ReboundChampRace(reboundsPerGame)
    elif choice=="4":
        BlockChampRace(blocksPerGame)
    elif choice=="5":
        StealsChampRace(stealsPerGame)
    else:
        on=False
        print("invalid input\n Goodbye!")
    
        