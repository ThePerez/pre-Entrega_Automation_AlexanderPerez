from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.boton_agregar = (By.CLASS_NAME, "btn_inventory")
        self.icono_carrito = (By.CLASS_NAME, "shopping_cart_badge")
        self.link_carrito = (By.CLASS_NAME, "shopping_cart_link")
        self.producto_en_carrito = (By.CLASS_NAME, "inventory_item_name")

    def agregar_primer_producto(self):
        self.driver.find_elements(*self.boton_agregar)[0].click()

    def contador_carrito(self):
        return self.driver.find_element(*self.icono_carrito).text

    def ir_al_carrito(self):
        self.driver.find_element(*self.link_carrito).click()

    def obtener_nombre_producto_en_carrito(self):
        return self.driver.find_element(*self.producto_en_carrito).text    