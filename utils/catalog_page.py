from selenium.webdriver.common.by import By

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.titulo = (By.CLASS_NAME, "title")
        self.productos = (By.CLASS_NAME, "inventory_item")
        self.menu = (By.ID, "react-burger-menu-btn")
        self.filtros = (By.CLASS_NAME, "product_sort_container")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link") 
    
    # 1. Valida el título
    def obtener_titulo(self):
        return self.driver.find_element(*self.titulo).text

    # 2. MÉTODO REQUERIDO POR test_catalogo
    def contar_productos(self):
        # Incluye este método si lo usas en tu test_catalogo para validar la cuenta.
        return len(self.driver.find_elements(*self.productos))

    # 3. MÉTODO REQUERIDO POR test_cart
    def agregar_primer_producto_al_carrito(self):        
        productos = self.driver.find_elements(*self.productos) 
        
        if not productos:
            raise Exception("No se encontraron productos para agregar al carrito.")

        primer_producto = productos[0]
        add_to_cart_button = primer_producto.find_element(By.XPATH, ".//button[text()='Add to cart']")
        
        # 3. Obtener el nombre para validación
        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        
        # 4. Hacer clic
        add_to_cart_button.click()        
        return nombre # Devolvemos el nombre del producto agregado

    # 4. MÉTODO REQUERIDO POR test_cart
    def navegar_a_carrito(self):
        self.driver.find_element(*self.cart_icon).click()
