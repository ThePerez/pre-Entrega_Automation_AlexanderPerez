import pytest
import logging
import pathlib
from utils.logger import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage 

# 1. Desactivar los logs de webdriver-manager para evitar conflictos en Pytest
logging.getLogger('webdriver_manager').setLevel(logging.WARNING) 


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    
    # 🔑 La instalación devuelve la ruta del driver compatible (SOLUCIÓN CRÍTICA)
    driver_path = ChromeDriverManager().install() 
    service = Service(driver_path) 

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()


@pytest.fixture
def login_exitoso(driver):
    # ... (el resto del código de login_exitoso es correcto)
    login_page = LoginPage(driver)
    inventory_page = login_page.login_completo('standard_user', 'secret_sauce') 
    return inventory_page

# Carpeta para capturas
SCREENSHOT_DIR = pathlib.Path('reports/screens')
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # Ejecutamos el test y obtenemos el resultado
    outcome = yield
    report = outcome.get_result()

    # Si es la fase de ejecución ('call') y falló ('failed')
    if report.when == 'call' and report.failed:
        # Intentamos obtener el driver del test
        driver = item.funcargs.get('driver') or item.funcargs.get('login_exitoso')
        
        # A veces el driver está dentro de un objeto Page, intentamos buscarlo
        if not driver:
            # Búsqueda genérica de driver en los argumentos
            for arg in item.funcargs.values():
                if hasattr(arg, 'driver'):
                    driver = arg.driver
                    break

        if driver:
            # Nombre del archivo: test_nombre.png
            file_name = f"{item.name}.png"
            file_path = SCREENSHOT_DIR / file_name
            
            # Tomar captura
            driver.save_screenshot(str(file_path))
            logger.error(f"[FALLO] Test: {item.name}. Captura guardada en {file_path}")
            
            # Adjuntar al reporte HTML (si pytest-html está instalado)
            if hasattr(report, 'extra'):
                from pytest_html import extras
                report.extra.append(extras.image(str(pathlib.Path('screens') / file_name)))