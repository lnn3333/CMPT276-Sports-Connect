import http.client
import json

#Below was done with the help of the SportsRadar API documentation
url = "/soccer/trial/v4/en/seasons/sr:season:105353/leaders.json?api_key=a9wpvfq5favxzvxe4w9dj74m"

conn = http.client.HTTPSConnection("api.sportradar.us")
conn.request("GET", url)

response = conn.getresponse()
data = response.read()

decodedData=data.decode("utf-8")
conn.close()

socLeadJSON = json.loads(decodedData)

#store JSON data
with open ("socLeaders.json","w") as file:
    json.dump(socLeadJSON,file,indent=4)

#read JSON data
with open("socLeaders.json","r") as reading:
    SocData = json.load(reading)
    
for list in SocData['lists']:
    if list['type'] == 'goals':
        goldenBoot = list
    elif list['type'] == 'assists':
        assistLeader = list

# function to format the name so it goes from [lastName, firstName] to firstName lastName
def formatName(name):
    nameLength = len(name.split(", "))
    
    # if the name as one first name and one last name
    if nameLength == 2:
        lastName,firstName = name.split(", ")
        formattedName = f"{firstName} {lastName}"
   
    #if only one name Ex. Fred
    elif nameLength == 1:
        formattedName = name
    
    #if name has 2 parts to last name
    elif nameLength == 3:
        lastName = name.split(", ")[-1]
        firstName = ' '.join(name.split(", ")[:-1])
        formattedName = f"{firstName} {lastName}"
    return formattedName

def goldenBootRace(list):
    #if list exists
    if list is not None:
       race =list['leaders']
       print("Top 10 in goals:")
       i=0
       for leader in race:
           for player in leader['players'][:10]:
               #Only printing the top 10 
                if i==10:
                    break
                else:
                    i+=1  
                    name=formatName(player['name'])
                    print(f"{i}.{name} - {player['competitors'][0]['datapoints'][0]['value']} Goals")  
    else:
        print("Category not found.")

def assistLeaderRace(list):
    #if list exists
    if list is not None:
       race =list['leaders']
       print("Top 10 in Assists:")
       i=0 # counter to only print top 10
       for leader in race:
           for player in leader['players'][:10]:
               #Only printing the top 10 
                if i==10:
                    break
                else:
                    i+=1  
                    name=formatName(player['name'])
                    print(f"{i}.{name} - {player['competitors'][0]['datapoints'][0]['value']} Assists")  
    else:
        print("Category not found.")
on = True
while on:
    print("=========================================")
    choice=input("Please chose one of the following:\n1.Top scorers\n2.Top assisters\n")
    if choice=="1":
        goldenBootRace(goldenBoot)
    elif choice=="2":
        assistLeaderRace(assistLeader)
    else:
        on=False
        print("Exiting...Goodbye!")