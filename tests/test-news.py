import unittest
import json
from news_api import getNews

class TestNewsFunctions(unittest.TestCase):

    def setUp(self):
        with open("sample-newsData.json","r") as reading:
            self.newsData = json.load(reading)
        
    def testGetNews(self):    
        newsArticles = getNews(self.newsData)
        self.assertIsNotNone(newsArticles)

if __name__ == '__main__':
    unittest.main()