from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    
    # --- Localizadores ---
    _INVENTORY_TITLE = (By.CSS_SELECTOR, ".title")
    _CART_ICON = (By.CSS_SELECTOR, ".shopping_cart_link") # Modificado para ser más general
    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    _FIRST_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    _FIRST_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _FIRST_ADD_TO_CART_BTN = (By.XPATH, "(//button[text()='Add to cart'])[1]") 
    
    # LOCATOR DINÁMICO (manteniendo tu implementación)
    def ADD_TO_CART_BTN(self, product_name):
        return (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[text()='Add to cart']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Métodos de Verificación (para test_catalogo_valido) ---
    
    def obtener_titulo(self):
        # El test usa obtener_titulo, no get_title_text
        return self.wait.until(EC.visibility_of_element_located(self._INVENTORY_TITLE)).text
    
    def contar_productos(self):
        return len(self.driver.find_elements(*self._INVENTORY_ITEMS))

    def obtener_primer_producto(self):
        """Retorna el nombre y el precio del primer producto de la lista."""
        nombre = self.driver.find_element(*self._FIRST_ITEM_NAME).text
        precio = self.driver.find_element(*self._FIRST_ITEM_PRICE).text
        return nombre, precio

    # --- Métodos de Flujo (para test_agregar_producto_y_navegar_a_carrito) ---

    def agregar_primer_producto_al_carrito(self):
        """Agrega el primer producto al carrito y retorna su nombre."""
        nombre_producto = self.obtener_primer_producto()[0]
        self.driver.find_element(*self._FIRST_ADD_TO_CART_BTN).click()
        return nombre_producto
        
    def navegar_a_carrito(self):
        """Navega al carrito y retorna el Page Object del carrito (CartPage)."""
        self.driver.find_element(*self._CART_ICON).click()
        
        # Importación diferida
        from pages.cart_page import CartPage
        return CartPage(self.driver)