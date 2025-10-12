from selenium.webdriver.common.by import By
class CartPage:
    def __init__(self, driver):
        self.driver = driver       
        self.cart_items = (By.CLASS_NAME, "cart_item")
        
    def verificar_producto_por_nombre(self, nombre_esperado):        
        items = self.driver.find_elements(*self.cart_items)
        
        for item in items:
            nombre_en_carrito = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            
            if nombre_en_carrito == nombre_esperado:
                return True 
        
        return False # No se encontró después de revisar todos los ítems