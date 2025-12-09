import time
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
        self.wait = WebDriverWait(driver, 20)

    def completar_informacion(self, nombre: str, apellido: str, codigo_postal: str):
        self.wait.until(EC.visibility_of_element_located(self._FIRST_NAME_INPUT)).send_keys(nombre)
        self.driver.find_element(*self._LAST_NAME_INPUT).send_keys(apellido)
        self.driver.find_element(*self._POSTAL_CODE_INPUT).send_keys(codigo_postal)
        return self

    def continuar_a_overview(self):
        # 1. Esperar a que el botón sea visible e interactuable
        boton = self.wait.until(EC.element_to_be_clickable(self._CONTINUE_BUTTON))
        
        # 🔑 TRUCO FINAL: Pequeña pausa para asegurar que los inputs se registraron
        # (Necesario por la latencia de OneDrive/Sistema cargado)
        time.sleep(1)
        
        # 2. Clic forzado con JavaScript (Infalible)
        self.driver.execute_script("arguments[0].click();", boton)
        
        # 3. Esperar cambio de URL
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        
        from pages.checkout_overview_page import CheckoutOverviewPage
        return CheckoutOverviewPage(self.driver)