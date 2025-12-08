from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    URL = "https://www.saucedemo.com/"

    # Localizadores
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']") 

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)
        return self

    def completar_usuario(self, usuario: str):
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        campo.clear()
        campo.send_keys(usuario)
        return self

    def completar_clave(self, clave: str):
        campo = self.wait.until(EC.visibility_of_element_located(self._PASS_INPUT))
        campo.clear()
        campo.send_keys(clave)
        return self

    def hacer_clic_login(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self
    
    # Métodos de verificación para la parametrización de error
    def esta_error_visible(self) -> bool:
        try:
            wait_error = WebDriverWait(self.driver, 3) 
            wait_error.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return True
        except TimeoutException:
            return False

    def obtener_mensaje_error(self) -> str:
        if self.esta_error_visible():
            return self.driver.find_element(*self._ERROR_MESSAGE).text
        return ""    

    def login_completo(self, usuario, clave):
        self.abrir()
        self.completar_usuario(usuario)
        self.completar_clave(clave)
        self.hacer_clic_login()
        
        self.wait.until(EC.url_to_be(self.URL + "inventory.html"))

        from pages.inventory_page import InventoryPage 
        return InventoryPage(self.driver) # Ahora InventoryPage está definida aquí