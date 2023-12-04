import unittest
from app import app

# integration tests to ensure the web app returns a 200 code (request was successful)
class TestIntegrationApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def testHomePage(self):
        webResponse = self.app.get("/")
        code = webResponse.status_code
        self.assertEqual(code,200)
        
    def testAwardRaces(self):
        webResponse = self.app.get("/nbaAwards")
        code = webResponse.status_code
        self.assertEqual(code,200)
        
    def testSchedule(self):
        webResponse = self.app.get("/schedule")
        code = webResponse.status_code
        self.assertEqual(code,200)

    def testteamList(self):
        webResponse = self.app.get("/team")
        code = webResponse.status_code
        self.assertEqual(code,200)        

    def testteamSchedule(self):
        webResponse = self.app.get("/team-schedule")
        code = webResponse.status_code
        self.assertEqual(code,200)
        
    def testpastSeason(self):
        webResponse = self.app.get("/pastSeason")
        code = webResponse.status_code
        self.assertEqual(code,200)        
        