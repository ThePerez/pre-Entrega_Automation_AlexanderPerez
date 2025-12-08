# pages/checkout_information_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutInformationPage:
    URL = "https://www.saucedemo.com/checkout-step-one.html"
    
    _FIRST_NAME_INPUT = (By.ID, "first-name")
    _LAST_NAME_INPUT = (By.ID, "last-name")
    _POSTAL_CODE_INPUT = (By.ID, "postal-code")
    _CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def completar_informacion(self, nombre: str, apellido: str, codigo_postal: str):
        self.wait.until(EC.visibility_of_element_located(self._FIRST_NAME_INPUT)).send_keys(nombre)
        self.driver.find_element(*self._LAST_NAME_INPUT).send_keys(apellido)
        self.driver.find_element(*self._POSTAL_CODE_INPUT).send_keys(codigo_postal)
        return self

    def continuar_a_overview(self):
        self.driver.find_element(*self._CONTINUE_BUTTON).click()
        
        # Importación diferida
        from pages.checkout_overview_page import CheckoutOverviewPage
        return CheckoutOverviewPage(self.driver)