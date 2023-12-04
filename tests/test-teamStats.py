import unittest
import json
from teamStatisticsNBA import get_teams, list_matches, get_team_stats
from teamProfileNBA import get_teamID
class testTeamStats(unittest.TestCase):

    def setUp(self):
        # replicating the readTeamData
        with open("tests/sample-teamStatsNBA.json", "r") as file:
            self.games = json.load(file)
    
    def testget_teams(self):
        listOfTeams = get_teams()
        print(listOfTeams)
        self.assertGreater(len(listOfTeams), 0, "The list is empty")
    
    def testlist_matches(self):
        # team id for the LA clippers
        games = list_matches(1610612746)
        self.assertGreater(len(games), 0, "The list is empty")
        
    def testget_team_stats(self):
        games = list_matches(1610612746)
        statList = []
        for _,gameID in games:
            teamStats = get_team_stats(gameID)
            statList.append(teamStats)
            # prints pts from each game
            print(teamStats["PTS"])
        self.assertGreater(len(statList), 0, "The list is empty")
        
if __name__ == '__main__':
    unittest.main()