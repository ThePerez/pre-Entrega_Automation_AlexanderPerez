from selenium.webdriver.common.by import By

class InventoryPage:
    # Locators de CatalogPage
    INVENTORY_TITLE = (By.CSS_SELECTOR, ".title")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    
    # LOCATOR DINÁMICO para el botón
    def ADD_TO_CART_BTN(self, product_name):
        return (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button[text()='Add to cart']")

    def __init__(self, driver):
        self.driver = driver

    def get_title_text(self):
        return self.driver.find_element(*self.INVENTORY_TITLE).text
        
    def verify_url(self):
        # Asume la URL de la página de inventario
        assert "inventory.html" in self.driver.current_url

    def add_item_to_cart(self, product_name):
        locator = self.ADD_TO_CART_BTN(product_name)
        self.driver.find_element(*locator).click()
        
    def get_cart_count(self):
        try:
            # Espera a que el contador sea visible si no lo está
            element = self.driver.find_element(*self.CART_BADGE)
            return element.text
        except:
            return "0"