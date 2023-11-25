import http.client
import json

#Below was done with the help of the SportsRadar API documentation
url = "/nba/trial/v8/en/seasons/2023/REG/leaders.json?api_key=2595gy5scfm5sgje8fa4de36"

conn = http.client.HTTPSConnection("api.sportradar.us")
conn.request("GET", url)

response = conn.getresponse()
data = response.read()

decodedData=data.decode("utf-8")
conn.close()

LeadersJSON = json.loads(decodedData)

#store JSON data
with open ("NBALeaders.json","w") as file:
    json.dump(LeadersJSON,file,indent=4)

#read JSON data
def readData():
    with open("NBALeaders.json","r") as reading:
        DataSc = json.load(reading)
    return DataSc
   
def getCategories(DataSc):
    for category in DataSc['categories']:
        # Scoring champ
        if category['name'] == 'points' and category['type'] == 'average':
            pointsPerGame = category
        # Assist champ
        elif category['name'] == 'assists' and category['type'] == 'average':
            assistPerGame = category
        # Rebounding Champ
        elif category['name'] == 'rebounds' and category['type'] == 'average':
            reboundsPerGame = category
        # Block Champ
        elif category['name'] == 'blocks' and category['type'] == 'average':
            blocksPerGame = category
        # Steals Champ
        elif category['name'] == 'steals' and category['type'] == 'average':
            stealsPerGame = category
    return pointsPerGame, assistPerGame,reboundsPerGame, blocksPerGame, stealsPerGame

#functions to print out to terminal the top 5 in each of the 5 major categories
def scoringChampRace(pointsPerGame):
    if pointsPerGame is not None:
        ranks = pointsPerGame['ranks'][:5]
        i=0
        #print("Top 5:")
        for rank in ranks:
            if i==5:
                break
            else:
                i+=1
                #print(f"{i}.{rank['player']['full_name']}   {rank['score']} PPG")
    else:
        print("Category not found.")

def assistChampRace(assistPerGame):
    if assistPerGame is not None:
        ranks = assistPerGame['ranks'][:5]
        i=0
        #print("Top 5:")
        for rank in ranks:
            if i==5:
                break
            else:
                i+=1
                #print(f"{i}.{rank['player']['full_name']}   {rank['score']} APG")
    else:
        print("Category not found.")

def ReboundChampRace(reboundsPerGame):
    if reboundsPerGame is not None:
        ranks = reboundsPerGame['ranks'][:5]
        i=0
        #print("Top 5:")
        for rank in ranks:
            if i==5:
                break
            else:
                i+=1
                #print(f"{i}.{rank['player']['full_name']}   {rank['score']} RPG")
    else:
        print("Category not found.")

def BlockChampRace(blocksPerGame):
    if blocksPerGame is not None:
        ranks = blocksPerGame['ranks'][:5]
        i=0
        #print("Top 5:")
        for rank in ranks:
            if i==5:
                    break
            else:
                i+=1
                #print(f"{i}.{rank['player']['full_name']}   {rank['score']} BPG")
    else:
        print("Category not found.")

def StealsChampRace(stealsPerGame):
    if stealsPerGame is not None:
        ranks = stealsPerGame['ranks'][:5]
        i=0
        print("Top 5:")
        for rank in ranks:
            if i==5:
                    break
            else:
                i+=1
                #print(f"{i}.{rank['player']['full_name']}   {rank['score']} SPG")
    else:
        print("Category not found.")


    
        