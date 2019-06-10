import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
   @classmethod
   def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='C:\TestFile\chromedriver.exe')

   def setUp(self):
       pass
       #print('Robię przygotowanie przed testami')

   def test_demo_login(self):
       driver = self.driver
       driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
       title = driver.title
       print(title)
       assert 'Demobank - Bankowość Internetowa - Logowanie' == title

   def test_demo_accounts(self):
       title = 20
       print(f'Actual title: {title}')
       assert 'Demobank - Bankowość Internetowa - Konta' == title

   def test_demo_pulpit(self):
       driver = self.driver
       driver.get('https://demobank.jaktestowac.pl/pulpit.html')
       title = driver.title
       print(title)
       assert 'Demobank - Bankowość Internetowa - Pulpit' == title

   def test_transfer(self):
       driver = self.driver
       driver.get('https://demobank.jaktestowac.pl/przelew_nowy_zew.html')
       title = driver.title
       print(title)
       assert 'Demobank - Bankowość Internetowa - Przelew' == title

   def tearDown(self):
       # self.driver.quit()
       pass

   @classmethod
   def tearDownClass(self):
       self.driver.quit()