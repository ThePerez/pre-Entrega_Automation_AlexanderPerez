from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    URL = "https://www.saucedemo.com/cart.html"
    
    _CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verificar_producto_por_nombre(self, nombre_esperado: str) -> bool:
        
        # Busca todos los elementos de nombre de producto en el carrito
        productos_en_carrito = self.driver.find_elements(*self._CART_ITEM_NAME)
        
        for producto in productos_en_carrito:
            if producto.text == nombre_esperado:
                return True
        return False

    def iniciar_checkout(self):
        self.driver.find_element(*self._CHECKOUT_BUTTON).click()
        
        # Importación diferida para evitar dependencias circulares
        from pages.checkout_information_page import CheckoutInformationPage
        return CheckoutInformationPage(self.driver)