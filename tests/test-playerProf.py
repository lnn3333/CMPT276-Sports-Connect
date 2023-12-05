import unittest
import json
from datetime import datetime
from playerProfileNBA import list_players, get_players_full_name, get_playerID

class testPlayerProfile(unittest.TestCase):
    def setUp(self):
        with open("tests/sample-playerProfile.json", "r") as file:
            self.players = json.load(file)
    
    def testlist_players(self):
        list=list_players()
        #print(list[:50])
        self.assertGreater(len(list), 0, "The list is empty")
        
    #find info about karl anthony towns
    def testget_players_full_name(self):
        playerInfo = get_players_full_name("Karl-Anthony Towns")
        name = playerInfo["name"]
        bday = playerInfo["bday"]
        h=playerInfo["height"]
        w=playerInfo["weight"]
        country=playerInfo["country"]
        num=playerInfo["jersey"]
        position=playerInfo["pos"]
        team=playerInfo["team"]
        print(name,bday,h,w,country,num,team)
        self.assertEqual(name,"Karl-Anthony Towns")
        self.assertEqual(bday,"November 15, 1995")
        self.assertEqual(h,"7 ft 0")
        self.assertEqual(w,"248")
        self.assertEqual(country,"USA")
        self.assertEqual(num,"32")
        self.assertEqual(team,"Timberwolves")

if __name__ == '__main__':
    unittest.main()