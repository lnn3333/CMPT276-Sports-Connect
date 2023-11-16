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
with open("NBALeaders.json","r") as reading:
    DataSc = json.load(reading)
   
   #find and store a set of data correnspoinding to the apporiate statistical race
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

#functions to print out to terminal the top 10 in each of the 5 major categories
def scoringChampRace(pointsPerGame):
    if pointsPerGame is not None:
        ranks = pointsPerGame['ranks'][:10]
        i=0
        print("Top 10:")
        for rank in ranks:
            if i==10:
                break
            else:
                i+=1
                print(f"{i}.{rank['player']['full_name']}   {rank['score']} PPG")
    else:
        print("Category not found.")

def assistChampRace(assistPerGame):
    if assistPerGame is not None:
        ranks = assistPerGame['ranks'][:10]
        i=0
        print("Top 10:")
        for rank in ranks:
            if i==10:
                break
            else:
                i+=1
                print(f"{i}.{rank['player']['full_name']}   {rank['score']} APG")
    else:
        print("Category not found.")

def ReboundChampRace(reboundsPerGame):
    if reboundsPerGame is not None:
        ranks = reboundsPerGame['ranks'][:10]
        i=0
        print("Top 10:")
        for rank in ranks:
            if i==10:
                break
            else:
                i+=1
                print(f"{i}.{rank['player']['full_name']}   {rank['score']} RPG")
    else:
        print("Category not found.")

def BlockChampRace(blocksPerGame):
    if blocksPerGame is not None:
        ranks = blocksPerGame['ranks'][:10]
        i=0
        print("Top 10:")
        for rank in ranks:
            if i==10:
                    break
            else:
                i+=1
                print(f"{i}.{rank['player']['full_name']}   {rank['score']} BPG")
    else:
        print("Category not found.")

def StealsChampRace(stealsPerGame):
    if stealsPerGame is not None:
        ranks = stealsPerGame['ranks'][:10]
        i=0
        print("Top 10:")
        for rank in ranks:
            if i==10:
                    break
            else:
                i+=1
                print(f"{i}.{rank['player']['full_name']}   {rank['score']} SPG")
    else:
        print("Category not found.")

#Some testing to see if stats are accurate compared to NBA.com/stats
on = True
while on:
    print("=========================================")
    choice=input("Please chose one of the following:\n1.Scoring champ race\n2.Assist champ race \n3.Rebound champ race \n4.Block champ race \n5.Steal champ race\n")
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
        print("Exiting...Goodbye!")
    
        