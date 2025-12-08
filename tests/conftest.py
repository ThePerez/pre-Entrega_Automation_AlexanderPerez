# tests/conftest.py

import pytest
import logging # <-- ¡Nueva Importación!
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