from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    URL = "https://www.saucedemo.com/checkout-step-two.html"
    
    _FINISH_BUTTON = (By.ID, "finish")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_nombre_producto(self) -> str:      
        # Espera a que el elemento sea visible y obtiene su texto, limpiándolo.
        return self.wait.until(EC.visibility_of_element_located(self._ITEM_NAME)).text.strip()
    
    def finalizar_compra(self):
        # 1. 🔑 Corrección: Esperar a que el botón sea CLICKABLE antes de hacer clic
        self.wait.until(EC.element_to_be_clickable(self._FINISH_BUTTON)).click()
        
        # 2. Esperar la redirección (esto ya lo tenías)
        self.wait.until(EC.url_contains("checkout-complete.html"))
        
        from pages.checkout_complete_page import CheckoutCompletePage
        return CheckoutCompletePage(self.driver)