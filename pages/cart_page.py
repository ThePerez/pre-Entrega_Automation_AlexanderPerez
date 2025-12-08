from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.checkout_information_page import CheckoutInformationPage 

class CartPage:
    URL = "https://www.saucedemo.com/cart.html"
    
    # Localizadores
    _CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verificar_producto_por_nombre(self, nombre_esperado: str) -> bool:        

        productos_en_carrito = self.driver.find_elements(*self._CART_ITEM_NAME)
        
        for producto in productos_en_carrito:
            if producto.text == nombre_esperado:
                return True
        return False

    def iniciar_checkout(self) -> CheckoutInformationPage:

        self.driver.find_element(*self._CHECKOUT_BUTTON).click()

        self.wait.until(EC.url_contains("/checkout-step-one.html")) 

        return CheckoutInformationPage(self.driver)