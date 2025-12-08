from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 

class CheckoutCompletePage:
    URL = "https://www.saucedemo.com/checkout-complete.html"
    
    _HEADER_MESSAGE = (By.CLASS_NAME, "complete-header") 

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def obtener_mensaje_cabecera(self) -> str:
        # 🔑 CORRECCIÓN 1: Usamos .strip() para limpiar cualquier espacio/salto de línea.
        return self.wait.until(EC.visibility_of_element_located(self._HEADER_MESSAGE)).text.strip()

    def es_pagina_de_confirmacion(self) -> bool:
        try:
            self.wait.until(EC.url_to_be(self.URL))         
            mensaje = self.obtener_mensaje_cabecera()           
            return mensaje.upper() == "THANK YOU FOR YOUR ORDER"        
        except TimeoutException:

            return False