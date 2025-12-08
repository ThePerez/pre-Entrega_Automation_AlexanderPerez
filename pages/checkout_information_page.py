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
        # Aumentamos a 30 segundos para máxima seguridad
        self.wait = WebDriverWait(driver, 30)

    def completar_informacion(self, nombre: str, apellido: str, codigo_postal: str):
        self.wait.until(EC.visibility_of_element_located(self._FIRST_NAME_INPUT)).send_keys(nombre)
        self.driver.find_element(*self._LAST_NAME_INPUT).send_keys(apellido)
        self.driver.find_element(*self._POSTAL_CODE_INPUT).send_keys(codigo_postal)
        return self

    def continuar_a_overview(self):
        # 1. Esperar a que el botón exista
        boton = self.wait.until(EC.element_to_be_clickable(self._CONTINUE_BUTTON))        

        # Esto evita que Selenium falle si el botón parece "tapado" o lento
        self.driver.execute_script("arguments[0].click();", boton)
        
        # 2. Esperar cambio de URL
        self.wait.until(EC.url_contains("checkout-step-two.html"))
        
        # Importación diferida
        from pages.checkout_overview_page import CheckoutOverviewPage
        return CheckoutOverviewPage(self.driver)