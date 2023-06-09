import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.keys import Keys
from time import sleep


# Dane testowe
email = "antekrrr.pl"
correct_email = "vw1302@o2.pl"
password = "zalozenie.konta"
incorrect_password = "gu"

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        # Warunki wstępne
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
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
           #scroll
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        sleep(1)
        self.driver.find_element(By.XPATH, '//button[@class="UIButtonScss-container-1RC"]').click()

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

    def testNoEmail_2(self):
        # 1. Nie wpisuje adresu email
        # 2. Wpisuje hasło
        password_input = self.driver.find_element(By.ID, 'createAccoutFormId_password')
        password_input.send_keys(password)
        # 3. Potwierdz hasło
        password_confirm = self.driver.find_element(By.ID, 'createAccoutFormId_confirm')
        password_confirm.send_keys(password)
        sleep(2)
        # 4. Zaznacz „ Zapoznałem się i akceptuję regulamin sklepu internetowego.”
        statement_checkbox = self.driver.find_element(By.XPATH, '//div[@id="2058"]/button')
        statement_checkbox.click()
        sleep(2)
        # 5. Kliknij "Załóż konto"
            # scroll
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        sleep(1)
        self.driver.find_element(By.XPATH, '//button[@class="UIButtonScss-container-1RC"]').click()


        #  SPRAWDZENIE OCZEKIWANEGO REZULTATU
        # 1. Szukam wszytkich komunikatów o błędzie
        error_messages = self.driver.find_elements(By.XPATH, '//span[@class="UIFormErrorMessageScss-root-2N8"]')
        # 2. Sprawdzam, czy jest jeden komunikat o błędzie
        error_msg_locator = locate_with(By.XPATH, '//span[@class="UIFormErrorMessageScss-root-2N8"]').near( {By.ID: 'createAccoutFormId_email'})
        error_msg = self.driver.find_element(error_msg_locator)
        # 4. Sprawdzam poprawność jego treści "Podaj adres e-mail!"
        assert error_messages[0].id == error_msg.id


    def testIncorrectPassword_3(self):
        # 1. Wpisz adres e-mail
        email_input = self.driver.find_element(By.ID, "createAccoutFormId_email")
        email_input.send_keys(correct_email)
        sleep(2)

        # 2. Wpisz hasło
        password_input = self.driver.find_element(By.ID, 'createAccoutFormId_password')
        password_input.send_keys(password)
        sleep(2)

        # 3. Potwierdz hasło
        password_confirm = self.driver.find_element(By.ID, 'createAccoutFormId_confirm')
        password_confirm.send_keys(incorrect_password)
        sleep(2)

        # 4. Zaznacz „ Zapoznałem się i akceptuję regulamin sklepu internetowego.”
        statement_checkbox = self.driver.find_element(By.XPATH, '//div[@id="2058"]/button')
        statement_checkbox.click()
        sleep(2)

        # 5. Kliknij "Załóż konto"
           # scroll
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        sleep(1)
        self.driver.find_element(By.XPATH, '//button[@class="UIButtonScss-container-1RC"]').click()


        #  SPRAWDZENIE OCZEKIWANEGO REZULTATU
        # 1. Szukam wszytkich komunikatów o błędzie
        error_messages = self.driver.find_elements(By.XPATH,
                                                   '//*[contains(text(), "Hasła nie pasują do siebie. Spróbuj ponownie.")]')
        # 2. Sprawdzam, czy jest jeden komunikat o błędzie
        self.assertEqual(1, len(error_messages))
        # 3. Sprawdzam, czy jest on pod polem "powtórz hasło"
        error_msg_locator = locate_with(By.XPATH, '//*[contains(text(), "Hasła nie pasują do siebie. Spróbuj ponownie.")]').near(
            {By.ID: 'createAccoutFormId_confirm'})
        error_msg = self.driver.find_element(error_msg_locator)
        # 4. Sprawdzam poprawność jego treści "Hasła nie pasują do siebie. Spróbuj ponownie"
        assert error_messages[0].id == error_msg.id

    def testNoConfirmPassword_4(self):
        # 1. Wpisz adres e-mail
        email_input = self.driver.find_element(By.ID, "createAccoutFormId_email")
        email_input.send_keys(correct_email)
        sleep(2)

        # 2. Wpisz hasło
        password_input = self.driver.find_element(By.ID, 'createAccoutFormId_password')
        password_input.send_keys(password)
        sleep(2)

        # 3. Potwierdz hasło

        # 4. Zaznacz „ Zapoznałem się i akceptuję regulamin sklepu internetowego.”
        statement_checkbox = self.driver.find_element(By.XPATH, '//div[@id="2058"]/button')
        statement_checkbox.click()
        sleep(2)

        # 5. Kliknij "Załóż konto"
           # scroll
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        sleep(1)
        self.driver.find_element(By.XPATH, '//button[@class="UIButtonScss-container-1RC"]').click()
        sleep(1)


        #  SPRAWDZENIE OCZEKIWANEGO REZULTATU
        # 1. Szukam wszytkich komunikatów o błędzie
        error_messages = self.driver.find_elements(By.XPATH,
                                                   '//span[@class="UIFormErrorMessageScss-root-2N8"]')
        # 2. Sprawdzam, czy jest jeden komunikat o błędzie
        self.assertEqual(1, len(error_messages))
        # 3. Sprawdzam, czy jest on pod polem "powtórz hasło"
        error_msg_locator = locate_with(By.XPATH, '//span[@class="UIFormErrorMessageScss-root-2N8"]').near(
            {By.ID: 'createAccoutFormId_confirm'})
        error_msg = self.driver.find_element(error_msg_locator)
        # 4. Sprawdzam poprawność jego treści "Pole potwierdź hasło jest wymagane."
        assert error_messages[0].id == error_msg.id

    def testCorrectNuberLetterInPassword_5(self):
        # 1. Wpisz adres e-mail
        email_input = self.driver.find_element(By.ID, "createAccoutFormId_email")
        email_input.send_keys(correct_email)
        sleep(2)

        # 2. Wpisz hasło
        password_input = self.driver.find_element(By.ID, 'createAccoutFormId_password')
        password_input.send_keys(incorrect_password)
        sleep(2)

        # 3. Potwierdz hasło
        password_confirm = self.driver.find_element(By.ID, 'createAccoutFormId_confirm')
        password_confirm.send_keys(incorrect_password)
        sleep(2)

        # 4. Zaznacz „ Zapoznałem się i akceptuję regulamin sklepu internetowego.”
        statement_checkbox = self.driver.find_element(By.XPATH, '//div[@id="2058"]/button')
        statement_checkbox.click()
        sleep(2)

        # 5. Kliknij "Załóż konto"
           # scroll
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        sleep(1)
        self.driver.find_element(By.XPATH, '//button[@class="UIButtonScss-container-1RC"]').click()

        #  SPRAWDZENIE OCZEKIWANEGO REZULTATU
        # 1. Szukam wszytkich komunikatów o błędzie
        error_messages = self.driver.find_elements(By.XPATH,
                                                   '//span[@class="UIFormErrorMessageScss-root-2N8"]')
        # 2. Sprawdzam, czy jest jeden komunikat o błędzie "Hasło musi zawierać co najmniej 8 znaków."
        self.assertEqual(1, len(error_messages))
        # 3. Sprawdzam, czy jest on pod polem " hasło"
        error_msg_locator = locate_with(By.XPATH,
                                        '//span[@class="UIFormErrorMessageScss-root-2N8"]').near(
            {By.ID: 'createAccoutFormId_password'})
        error_msg = self.driver.find_element(error_msg_locator)
        # 4. Sprawdzam poprawność jego treści "Hasło musi zawierać co najmniej 8 znaków."
        assert error_messages[0].id == error_msg.id

    def testAcceptance_6(self):
        # 1. Wpisz adres e-mail
        email_input = self.driver.find_element(By.ID, "createAccoutFormId_email")
        email_input.send_keys(correct_email)
        sleep(2)

        # 2. Wpisz hasło
        password_input = self.driver.find_element(By.ID, 'createAccoutFormId_password')
        password_input.send_keys(password)
        sleep(2)

        # 3. Potwierdz hasło
        password_confirm = self.driver.find_element(By.ID, 'createAccoutFormId_confirm')
        password_confirm.send_keys(password)
        sleep(2)

        # 4. Nie zaznacza „ Zapoznałem się i akceptuję regulamin sklepu internetowego.”


        # 5. Kliknij "Załóż konto"
            # scroll
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        sleep(1)
        self.driver.find_element(By.XPATH, '//button[@class="UIButtonScss-container-1RC"]').click()

        #  SPRAWDZENIE OCZEKIWANEGO REZULTATU
        # 1. Szukam wszytkich komunikatów o błędzie
        error_messages = self.driver.find_elements(By.XPATH,
                                                   '//div[@class="UIAgreementLabelScss-required-2mq"]')
        # 2. Sprawdzam, czy jest jeden komunikat o błędzie
        self.assertEqual(1, len(error_messages))

        # 3. Sprawdzam, czy jest on pod polem "Zapoznałem się i akceptuję regulamin sklepu internetowego."
        error_msg_locator = locate_with(By.XPATH,
                                        '//div[@class="UIAgreementLabelScss-required-2mq"]').near(
            {By.XPATH: '//div[@id="2058"]/button'})
        error_msg = self.driver.find_element(error_msg_locator)
        # 4. Sprawdzam poprawność jego treści "Hasła nie pasują do siebie. Spróbuj ponownie"
        assert error_messages[0].id == error_msg.id




    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
