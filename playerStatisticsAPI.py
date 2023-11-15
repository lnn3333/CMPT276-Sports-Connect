import http.client
import json

api_key = "bfjwx5umvmgrds4j57c6j3nz"
url = "/nba/trial/v8/en/players/ab532a66-9314-4d57-ade7-bb54a70c65ad/profile.json?api_key=" + api_key

conn = http.client.HTTPSConnection("api.sportradar.us")
conn.request("GET", url)

res = conn.getresponse()
data = res.read()

decodedData = data.decode("utf-8")
conn.close()

playerProfileJSON = json.loads(decodedData)

with open ("playerProfile.json","w") as file:
    json.dump(playerProfileJSON,file,indent=4)

with open("playerProfile.json","r") as reading:
    DataSc = json.load(reading)
