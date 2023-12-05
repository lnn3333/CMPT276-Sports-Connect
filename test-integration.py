import unittest
from app import app

# integration tests to ensure the web app returns a 200 code (request was successful)
class TestIntegrationApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    # News
    def testHomePage(self):
        webResponse = self.app.get("/")
        code = webResponse.status_code
        self.assertEqual(code,200)
    
    #Award Races  
    def testAwardRaces(self):
        webResponse = self.app.get("/nbaAwards")
        code = webResponse.status_code
        self.assertEqual(code,200)
    
    #Live Scores 
    def testSchedule(self):
        webResponse = self.app.get("/schedule")
        code = webResponse.status_code
        self.assertEqual(code,200)

    #List of Teams
    def testteamList(self):
        webResponse = self.app.get("/team")
        code = webResponse.status_code
        self.assertEqual(code,200)        

    #Search for Team Schedule
    def testteamSchedule(self):
        webResponse = self.app.get("/team-schedule")
        code = webResponse.status_code
        self.assertEqual(code,200)
      
    #Find player Profile  
    def testPlayerProfile(self):
        webResponse = self.app.get("/player-profile")
        code = webResponse.status_code
        self.assertEqual(code,200)        

    #Find Team Profile
    def testteamProfile(self):
        webResponse = self.app.get("/team-profile")
        code = webResponse.status_code
        self.assertEqual(code,200)
      
    #Finding past season  
    def testpastSeason(self):
        webResponse = self.app.get("/pastSeason")
        code = webResponse.status_code
        self.assertEqual(code,200)        
    
    #Player stats   
    def testplayerStats(self):
        webResponse = self.app.get("/player-statistics")
        code = webResponse.status_code
        self.assertEqual(code,200)               

    #Stats for a team 
    def testteamStats(self):
        webResponse = self.app.get("/team-statistics")
        code = webResponse.status_code
        self.assertEqual(code,200)
        