import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
    #@classmethod
    #def setUpClass(self):
        #self.driver = webdriver.Chrome(executable_path='C:\TestFile\chromedriver.exe')


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:\TestFile\chromedriver.exe')
        print ('poczatek testu')
        pass

    def test_strona_glowna(self):
        driver = self.driver
        driver.get('https://www.coveredcalendar.com/?ref=discuvver')
        title = driver.title
        print(title)
        assert title == 'CoveredCalendar.com'

    def test_podstrona_1(self):
        driver = self.driver
        driver.get('https://www.coveredcalendar.com/request-samples')
        title = driver.title
        print (title)
        assert title == 'Request Samples — CoveredCalendar.com'

    def test_podstrona_2(self):
        driver = self.driver
        driver.get('https://www.coveredcalendar.com/learn-more')
        title = driver.title
        print(title)
        assert title == 'CoveredCalendar.com'

    def tearDown(self):
        self.driver.quit()
        print('koniec testu')
        pass

    # @classmethod
    # def tearDownClass(self):
    #     #self.driver.quit()
    #     pass
