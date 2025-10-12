from selenium.webdriver.common.by import By

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.titulo = (By.CLASS_NAME, "title")
        self.productos = (By.CLASS_NAME, "inventory_item")
        self.menu = (By.ID, "react-burger-menu-btn")
        self.filtros = (By.CLASS_NAME, "product_sort_container")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link") # <-- NUEVO LOCALIZADOR

    # ... [Métodos existentes] ...

    # NUEVO MÉTODO
    def agregar_primer_producto_al_carrito(self):
        # 1. Obtener el contenedor del primer producto
        productos = self.driver.find_elements(*self.productos)
        if not productos:
            raise Exception("No se encontraron productos para agregar al carrito.")

        primer_producto = productos[0]
        
        # 2. Localizar el botón 'Add to cart' dentro del contenedor
        add_to_cart_button = primer_producto.find_element(By.CLASS_NAME, "btn_inventory")
        
        # 3. Obtener el nombre (lo usaremos para la validación final)
        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        
        # 4. Hacer clic
        add_to_cart_button.click()
        
        return nombre # Devolvemos el nombre del producto agregado

    # NUEVO MÉTODO
    def navegar_a_carrito(self):
        self.driver.find_element(*self.cart_icon).click()
