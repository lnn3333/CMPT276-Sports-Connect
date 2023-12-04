import unittest
from datetime import datetime, date, timezone
import json
from ScheduleNBA import getAllNBATeams,FindGamesForTeam, searchTeam, FormatDateTime, readData2,getImage

#Test to run check if games for Boston Celtics are found
class TestNBATools(unittest.TestCase):
    def setUp(self):
        with open("sample-NBAGames.json", "r") as file:
            self.gameData = json.load(file)
            
    def testreadData(self):
        data = readData2()
        self.assertIsNotNone(data)
        
    def test_FormatDateTime(self):
        time = "2023-11-08T06:30:00Z"
        formatted_date, formatted_time = FormatDateTime(time)
        print(formatted_date)
        print(formatted_time)
        self.assertEqual(formatted_date,date(2023,11,7))
        self.assertEqual(formatted_time,"10:30:00 PM")
    
    #find and print games for boston
    def testFindGamesForTeam(self):
        teamGames = FindGamesForTeam("BOS", self.gameData)
        self.assertGreater(len(teamGames), 0)
        for game in teamGames:
            print(f"{game['homeTeamName']} vs {game['awayTeamName']}")

    def testgetAllNBATeams(self):
        all_teams = getAllNBATeams(self.gameData)
        self.assertGreater(len(all_teams), 0)

    def testsearchTeam(self):
        teamAlias = searchTeam("Celtics", self.gameData)
        self.assertIsNotNone(teamAlias)

    def testgetImage(self):
        teamImage = getImage("Boston Celtics")
        self.assertIsNotNone(teamImage)

if __name__ == '__main__':
    unittest.main()