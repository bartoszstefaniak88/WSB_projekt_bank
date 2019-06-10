import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
    def test_main(self):
        driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe')
        driver.get('https://demobank.jaktestowac.pl/logowanie_prod.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Logowanie' == title
        driver.quit()
        pass