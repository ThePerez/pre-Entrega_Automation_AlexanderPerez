import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOverviewPage:
    URL = "https://www.saucedemo.com/checkout-step-two.html"
    
    _FINISH_BUTTON = (By.ID, "finish")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        # Aumentamos a 30s por seguridad
        self.wait = WebDriverWait(driver, 30)

    def obtener_nombre_producto(self) -> str:      
        return self.wait.until(EC.visibility_of_element_located(self._ITEM_NAME)).text.strip()
    
    def finalizar_compra(self):
        # 1. Esperar a que el botón sea visible e interactuable
        boton = self.wait.until(EC.element_to_be_clickable(self._FINISH_BUTTON))        
       
        time.sleep(1)      
      
        self.driver.execute_script("arguments[0].click();", boton)
        
        # 2. Esperar la redirección a la página final
        self.wait.until(EC.url_contains("checkout-complete.html"))
        
        from pages.checkout_complete_page import CheckoutCompletePage
        return CheckoutCompletePage(self.driver)