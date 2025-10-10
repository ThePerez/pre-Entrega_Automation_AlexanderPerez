import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from utils.login_page import LoginPage
from utils.catalog_page import CatalogPage
from utils.cart_page import CartPage    
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.login_page import LoginPage



@pytest.fixture 
def driver():
    # configuracion para consultar a selenium web driver
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_login(driver):
    # [1] Inicializar la Page Object
    login = LoginPage(driver) 
    
    # [2] Navegar a la página
    login.cargar_pagina() 
    
    # [3] Ingresar credenciales y hacer clic
    login.ingresar_usuario('standard_user')
    login.ingresar_contrasenia('secret_sauce')
    login.hacer_login()
    
    # [4] Validar login exitoso
       
    # Validar que la URL contenga '/inventory.html'
    assert "/inventory.html" in driver.current_url
    
    # Validar que el título de la pestaña (o página) contenga "Swag Labs"
    assert "Swag Labs" in driver.title 

#def test_catalogo():

    # logeo de usuario con username y password
    #click al boton de login 

    #podamos verificar el titulo pero del html

    #comprobar si existen productos en la pagina viosibles (len())
    #verificar elementos importantes de la pagina.

#def test_carrito():

    # logeo de usuario con username y password
    #click al boton de login 
    #llevarme a la pagina de carrito de compras
    #incremento de carrito al agregar un producto

    #comprobar que el carrito aparezca el produto correcta