from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutCompletePage:
    URL = "https://www.saucedemo.com/checkout-complete.html"
    
    _HEADER_MESSAGE = (By.CLASS_NAME, "complete-header") 

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def obtener_mensaje_cabecera(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self._HEADER_MESSAGE)).text

    def es_pagina_de_confirmacion(self) -> bool:
        return self.obtener_mensaje_cabecera() == "THANK YOU FOR YOUR ORDER"