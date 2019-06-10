import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='C:\TestFile\chromedriver.exe')

    def setUp(self):
        pass
        # print('Robię przygotowanie przed testami')

# Pobranie i porównanie nagłówka strony glownej (logowania)
    def test_demo_login(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Logowanie', title,
                         f'Oczekiwana wartosc title jest rozna od rzeczywistej na stronie {url}')

    # Pobranie i porównanie nagłówka  strony glownej konta
    def test_demo_accounts(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/konta.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Konta', title,
                         f'Oczekiwana wartosc title jest rozna od rzeczywistej na stronie {url}')

    # Pobranie i porównanie nagłówka  strony glownej po zalogowaniu uzytkownika
    def test_demo_pulpit(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/pulpit.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Pulpit', title,
                         f'Oczekiwana wartosc title jest rozna od rzeczywistej na stronie {url}')

    # Pobranie i porównanie nagłówka  storny tworzenia przelewu
    def test_transfer(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/przelew_nowy_zew.html'
        driver.get(url)
        title = driver.title
        print(f'Actual title: {title}')
        self.assertEqual('Demobank - Bankowość Internetowa - Przelew', title,
                         f'Oczekiwana wartosc title jest rozna od rzeczywistej na stronie {url}')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


class LoginPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="C:\TestFile\chromedriver.exe")


    def setUp(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)




#sprawdzenie poprawnosci naglowka po xPath
    def test_header(self):
        driver = self.driver
        naglowek = driver.find_element_by_xpath('//*[@id="login_form"]/h1')
        tekst_naglowka = naglowek.text
        self.assertEqual('Wersja demonstracyjna serwisu demobank', tekst_naglowka, 'oczykiwana wartość jest inna')


#spradzenie dostepnosci przycisku "dalej" dla loginu mniej niz 8 znakow i 8 znakow (poprawny)
    def test_button_next_disable(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        login_input_box = driver.find_element_by_xpath('//*[@id="login_id"]')
        login_7_znakow = login_input_box.send_keys('Bartek7')
        next_button = driver.find_element_by_xpath('//*[@id="login_next"]')
        next_button_disabled = next_button.get_property('disabled')
        self.assertEqual(True, next_button_disabled , f'bledna wartosc dla disabled jest: {next_button_disabled} powinno byc True dla mniej niz 7 znakow dla strony: {url}')
        time.sleep(1)
        login_input_box.clear()
        # 8 znakow
        login_8_znakow = login_input_box.send_keys('Bartekk8')
        time.sleep(1)
        next_button_disabled = next_button.get_property('disabled')
        self.assertEqual(False, next_button_disabled, f'bledna wartosc dla disabled powinno byc False dla 8 znakowna stronie: {url}')


# sprawdzenie wiadomości ostrzegawczej - ikona "pytajnik" na stronie logowania
    def test_zawartosc_komunikatu_dla_pytajnika(self):
        driver = self.driver
        login_input_box = driver.find_element_by_xpath('//*[@id="login_id"]')
        login_input_box.clear()
        login_mniej_znakow = login_input_box.send_keys('Bartek')
        pytajnik = driver.find_element_by_xpath('//*[@id="login_id_container"]/div[3]/div/i')
        pytajnik.click()
        pytajnik_tekst = pytajnik.get_property('textContent')
        print(f'tekst pytajnika: {pytajnik_tekst}')
        ostrzezenie_min_8_znakow = driver.find_element_by_xpath('//*[@class="error"]')
        tekst_ostrzezenie = ostrzezenie_min_8_znakow.text
        print(f'aktualny teskst ostrzegawczy dla pola login: {tekst_ostrzezenie}')
        print(len(driver.find_elements_by_xpath('//*[@class="i-hint-white tooltip widget-info"]')))
        self.assertEqual('identyfikator ma min. 8 znaków', tekst_ostrzezenie, 'tekst ostrzegawczy jest niepoprawny')


    def test_poprawnie_wpisany_login(self):
        driver = self.driver
        login_input_box = driver.find_element_by_xpath('//*[@id="login_id"]')
        login_input_box.clear()
        login_poprawna_ilosc_znakow = login_input_box.send_keys('Bartekk8')
        next_button = driver.find_element_by_xpath('//*[@id="login_next"]')
        next_button.click()
        time.sleep(3)
        next_button_new = driver.find_element_by_xpath('//*[@id="login_next"]')
        next_button_text = next_button_new.text
        print(f'aktualny tekst buttona zaloguj: {next_button_text}')
        self.assertEqual('zaloguj się', next_button_text, f'niepoprawny text dla login button, jest {next_button_text}')

#sprawdzenie porpawnosci komunikatu dla przypomnij identyfikator (tekst = ta funkcja jest niedostepna)
    def test_przypomnij_identyfikator(self):
        driver = self.driver
        przypomnij_identyfikator_button = driver.find_element_by_xpath('//*[@id="ident_rem"]')
        przypomnij_identyfikator_button.click()
        time.sleep(1)
        funkcja_niedostepna = driver.find_element_by_xpath('//*[@id="shadowbox"]/div/div/div/h2')
        #funkcja_niedostepna_text = funkcja_niedostepna.text
        #print(funkcja_niedostepna_text)
        self.assertEqual('ta funkcja jest niedostępna', funkcja_niedostepna.text, 'niepoprawny tekst komunikatu dla przypomnij identyfikator')
        zamknij_okono_funkcja_niedostepna = driver.find_element_by_xpath('//*[@id="shadowbox"]/div/i')
        zamknij_okono_funkcja_niedostepna.click()

#poprawne zalogowanie sie do banku
    def test_poprawne_zalogowanie(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_2.html'
        driver.get(url)
        login_input_box = driver.find_element_by_xpath('//*[@id="login_id"]')
        password_input_box = driver.find_element_by_xpath('//*[@id="login_password"]')
        login = login_input_box.send_keys('Bartekk8')
        password = password_input_box.send_keys('12345678')
        zaloguj_sie_button = driver.find_element_by_xpath('//*[@id="login_next"]')
        time.sleep(1)
        zaloguj_sie_button.click()
        time.sleep(1)
        zalogowany_konto_osobiste = driver.find_element_by_xpath('//*[@id="main_content"]/section/h1')
        print(f'poprawny tekst "konta osobiste": {zalogowany_konto_osobiste.text}')
        self.assertEqual('konta osobiste', zalogowany_konto_osobiste.text, 'naglowek konta osobistego niepoprawny')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

