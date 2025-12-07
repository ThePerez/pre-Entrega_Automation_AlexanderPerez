import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage # Importamos para usar la lógica de login

@pytest.fixture(scope="session")
def driver():
    """Configura y cierra el WebDriver para toda la sesión de pruebas."""
    options = Options()
    options.add_argument("--start-maximized")
    # Nota: Asegúrate de tener las importaciones necesarias para Service
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def login_exitoso(driver):
    """
    Fixture que realiza el login exitoso y devuelve la instancia de CatalogPage.
    Esto sirve como pre-condición limpia para cualquier test del catálogo o carrito.
    """
    # 1. Instanciar la página de Login
    login_page = LoginPage(driver)
    
    # 2. Ejecutar la acción completa de Login
    # Asumimos que login_completo retorna la siguiente Page Object (CatalogPage)
    catalog_page = login_page.login_completo('standard_user', 'secret_sauce')
    
    return catalog_page