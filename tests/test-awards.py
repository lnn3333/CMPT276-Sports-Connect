import unittest
import json

from AwardRacesNBA import readData, getCategories, scoringChampRace, assistChampRace, ReboundChampRace, BlockChampRace, StealsChampRace

class TestNBAAwardRace(unittest.TestCase):

    def setUp(self):
        with open("tests/sample-NBALeaders.json", "r") as file:
            self.leadersData = json.load(file)

    def testReadData(self):
        data = readData()
        self.assertIsNotNone(data)

    def testGetCategories(self):
        points, assists, rebounds, blocks, steals = getCategories(self.leadersData)
        self.assertIsNotNone(points)
        self.assertIsNotNone(assists)
        self.assertIsNotNone(rebounds)
        self.assertIsNotNone(blocks)
        self.assertIsNotNone(steals)
        
    def testScoringChampRace(self):
        points, _, _, _, _ = getCategories(self.leadersData)
        scoringChampRace(points)
        i=0
        for rank in points['ranks']:
            if i==30:
                break
            else:
                i+=1
                print(f"{i}.{rank['player']['full_name']}   {rank['score']} PPG")
    
    def testAssistChampRace(self):
        _, assists, _, _, _ = getCategories(self.leadersData)
        assistChampRace(assists)
        i=0
        for rank in assists['ranks']:
            if i==30:
                break
            else:
                i+=1
                print(f"{i}.{rank['player']['full_name']}   {rank['score']} APG")
                
    def testReboundChampRace(self):
        _, _, rebounds, _, _ = getCategories(self.leadersData)
        ReboundChampRace(rebounds)
        i=0
        for rank in rebounds['ranks']:
            if i==30:
                break
            else:
                i+=1
                print(f"{i}.{rank['player']['full_name']}   {rank['score']} RPG")
        

    def testBlockChampRace(self):
        _, _, _, blocks, _ = getCategories(self.leadersData)
        BlockChampRace(blocks)
        i=0
        for rank in blocks['ranks']:
            if i==30:
                break
            else:
                i+=1
                print(f"{i}.{rank['player']['full_name']}   {rank['score']} BPG")

    def testStealsChampRace(self):
        _, _, _, _, steals = getCategories(self.leadersData)
        StealsChampRace(steals)
        i=0
        for rank in steals['ranks']:
            if i==30:
                break
            else:
                i+=1
                print(f"{i}.{rank['player']['full_name']}   {rank['score']} SPG")
        

if __name__ == '__main__':
    unittest.main()
