import pytest
import time  # <-- ¡Asegúrate de que esta importación existe!
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from utils.login_page import LoginPage
from utils.catalog_page import CatalogPage
from utils.cart_page import CartPage  # Mantener si vas a desarrollar el test_carrito
# ... [Otras importaciones]

@pytest.fixture
def driver():
    # ... [Tu fixture 'driver' aquí] ...
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    yield driver
    # PAUSA final para ver el resultado antes de que el navegador se cierre
    time.sleep(5) 
    driver.quit()


def test_login(driver):
    print("\n[TEST] Ejecutando test_login...")
    login = LoginPage(driver)
    
    # [1] Navegar a la página
    login.cargar_pagina()
    time.sleep(5)  # PAUSA: Para ver la página de login
    
    # [2] Ingresar credenciales y hacer clic
    login.ingresar_usuario('standard_user')
    login.ingresar_contrasenia('secret_sauce')
    time.sleep(5)  # PAUSA: Para ver las credenciales ingresadas
    login.hacer_login()
    
    # [3] Validar login exitoso
    time.sleep(5)  # PAUSA: Para ver el catálogo cargado antes de la validación
    
    assert "/inventory.html" in driver.current_url
    assert "Swag Labs" in driver.title
    print("[SUCCESS] Test de Login completado.")


def test_catalogo(driver):
    """
    Obligatorio: Navegación y Verificación del Catálogo, incluyendo validación
    de la sección ('Products') y de la pestaña/marca ('Swag Labs').
    """
    
    # 1. Logeo (Pre-condición)
    print("\n[TEST] Ejecutando test_catalogo (Incluye Login)...")
    login = LoginPage(driver)
    login.cargar_pagina()
    login.ingresar_usuario('standard_user')
    login.ingresar_contrasenia('secret_sauce')
    login.hacer_login()
    time.sleep(5) 
    
    # 2. Inicializar la Page Object del Catálogo
    catalogo = CatalogPage(driver)
    
    # --- Verificación del Catálogo ---
    
    # 3. Validar el TÍTULO DE LA PESTAÑA/MARCA ('Swag Labs')
    print("[STEP] Validando el título de la pestaña del navegador...")
    assert "Swag Labs" in driver.title, \
        f"Fallo: El título de la pestaña no contiene 'Swag Labs'. Título actual: {driver.title}"
    print("[SUCCESS] Título de la pestaña ('Swag Labs') verificado correctamente.")
    time.sleep(5) 
    
    # 4. Validar el TÍTULO VISIBLE DE LA SECCIÓN ('Products')
    titulo_obtenido = catalogo.obtener_titulo()
    print(f"[STEP] Validando el título visible de la sección: '{titulo_obtenido}'...")
    
    assert titulo_obtenido == "Products", \
        f"Fallo: Se esperaba el título 'Products', pero se encontró '{titulo_obtenido}'."
    print("[SUCCESS] Título de la sección ('Products') verificado correctamente.")
    time.sleep(5)
    
    # 5. Comprobar existencia de productos
    num_productos = catalogo.contar_productos()
    print(f"[STEP] Validando presencia de productos. Encontrados: {num_productos}...")
    
    assert num_productos > 0
    print(f"[SUCCESS] Presencia de productos verificada. Se encontraron {num_productos} ítems.")
    time.sleep(5)
    
    # 6. Listar nombre y precio del primer producto
    product_name, product_price = catalogo.obtener_primer_producto()
    
    print(f"[INFO] Primer Producto Listado: Nombre = '{product_name}', Precio = '{product_price}'")
    
    # Validaciones finales
    assert len(product_name) > 0
    assert product_price.startswith("$")
    time.sleep(5) 
    print("[SUCCESS] Test de Catálogo completado.")
    
#def test_carrito():

    # logeo de usuario con username y password
    #click al boton de login 
    #llevarme a la pagina de carrito de compras
    #incremento de carrito al agregar un producto

    #comprobar que el carrito aparezca el produto correcta