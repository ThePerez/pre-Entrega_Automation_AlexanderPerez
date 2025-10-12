from selenium.webdriver.common.by import By
import time 

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        # LOCALIZADORES
        self.titulo = (By.CLASS_NAME, "title")
        self.productos = (By.CLASS_NAME, "inventory_item")
        self.menu = (By.ID, "react-burger-menu-btn")
        self.filtros = (By.CLASS_NAME, "product_sort_container")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link") 
    
    # MÉTODOS REQUERIDOS POR test_catalogo

    def obtener_titulo(self):
        """Retorna el título visible de la sección, ej: 'Products'."""
        return self.driver.find_element(*self.titulo).text

    def contar_productos(self):
        """Retorna el número de productos visibles en la lista."""
        return len(self.driver.find_elements(*self.productos))

    def obtener_primer_producto(self):
        """Retorna el nombre y precio del primer producto."""
        productos = self.driver.find_elements(*self.productos)
        if not productos:
            raise Exception("No se encontraron productos.")
        
        primer_producto = productos[0]
        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        return nombre, precio


    def agregar_primer_producto_al_carrito(self):
        productos = self.driver.find_elements(*self.productos) 
        if not productos:
            raise Exception("No se encontraron productos para agregar al carrito.")

        primer_producto = productos[0]
        # Localizador robusto con XPATH para el botón
        add_to_cart_button = primer_producto.find_element(By.XPATH, ".//button[text()='Add to cart']")
        
        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        add_to_cart_button.click()
        
        return nombre 

    def navegar_a_carrito(self):
        time.sleep(1)
        self.driver.find_element(*self.cart_icon).click()