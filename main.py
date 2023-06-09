import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys


# Dane testowe
email = "antekrrr.pl"
correct_email = "vw1302@o2.pl"
password = "zalozenie.konta"
incorrect_password = "gugu"

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        # Warunki wstępne
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #self.wait_10_seconds = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.neonet.pl")
        # 2. Niezalogowany Użytkownik
        # Zamknij okno cookies
        self.driver.find_element(By.XPATH,
        '//*[contains(text(),"Zaakceptuj wszystkie")][@class="cookiesBlockScss-action-1V0 uiSolidButtonCss-root-3aV "]').click()
        self.driver.implicitly_wait(20)
        # Kliknij w "Zaloguj się"
        zaloguj_btn = self.driver.find_element(By.XPATH, '//*[contains(text(),"Zaloguj się")]')
        zaloguj_btn.click()
        # Kliknij "Założ konto" - przekierowuje na rejestracje
        sleep(1)
        self.driver.find_element(By.XPATH,
                                 '//*[contains(text(),"Załóż konto")][@class="UIButtonScss-container-1RC UIButtonScss-ghost-2cK"]').click()


    def testWrongEmail_1(self):
        # 1. Wpisz adres e-mail
        email_input = self.driver.find_element(By.ID, "createAccoutFormId_email")
        email_input.send_keys(email)
        sleep(2)

        # 2. Wpisz hasło
        password_input = self.driver.find_element(By.ID, 'createAccoutFormId_password')
        password_input.send_keys(password)
        sleep(2)

        # 3. Potwierdz hasło
        password_confirm = self.driver.find_element(By.ID, 'createAccoutFormId_confirm')
        password_confirm.send_keys(password)
        sleep(2)

        # 4. Zaznacz „ Zapoznałem się i akceptuję regulamin sklepu internetowego.”
        statement_checkbox = self.driver.find_element(By.XPATH, '//div[@id="2058"]/button')
        statement_checkbox.click()
        sleep(2)

        # 5. Kliknij "Załóż konto"
           # Scrooll
        self.driver.find_element(By.TAG_NAME,"body").send_keys(Keys.PAGE_DOWN)

           #Nacisnąć
        sleep(5)
        self.driver.find_element(By.XPATH, '//button[@class="UIButtonScss-container-1RC"]').click()
        sleep(2)


        #self.driver.find_element(By.XPATH, '//button[contains(text(),"Załóż konto")]').click()
        #self.wait_10_seconds.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="createAccountScss-submitWrapper-2Qd"]'))).click()


        #  SPRAWDZENIE OCZEKIWANEGO REZULTATU
        # 1. Szukam wszytkich komunikatów o błędzie
        error_messages = self.driver.find_elements(By.XPATH, '//*[contains(text(), "Wprowadzono niepoprawny adres e-mail")]')
        # 2. Sprawdzam, czy jest jeden komunikat o błędzie
        self.assertEqual(1,len(error_messages))
        # 3. Sprawdzam, czy jest on pod polem "e-mail"
        error_msg_locator = locate_with(By.XPATH, '//*[contains(text(), "Wprowadzono niepoprawny adres e-mail")]').near({By.ID: 'createAccoutFormId_email'})
        error_msg = self.driver.find_element(error_msg_locator)
        # 4. Sprawdzam poprawność jego treści "Wprowadzono niepoprawny adres e-mail"
        assert error_messages[0].id == error_msg.id