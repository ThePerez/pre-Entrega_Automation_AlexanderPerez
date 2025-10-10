from selenium.webdriver.common.by import By

class CatalogPage:
    def __init__(self, driver):
        self.driver = driver
        self.titulo = (By.CLASS_NAME, "title")
        self.productos = (By.CLASS_NAME, "inventory_item")
        self.menu = (By.ID, "react-burger-menu-btn")
        self.filtros = (By.CLASS_NAME, "product_sort_container")

    def obtener_titulo(self):
        return self.driver.find_element(*self.titulo).text

    def contar_productos(self):
        return len(self.driver.find_elements(*self.productos))

    def obtener_primer_producto(self):
        producto = self.driver.find_elements(*self.productos)[0]
        nombre = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        return nombre, precio

    def menu_presente(self):
        return self.driver.find_element(*self.menu).is_displayed()

    def filtros_presentes(self):
        return self.driver.find_element(*self.filtros).is_displayed()
