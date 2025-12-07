# No necesita importar driver, ChromeDriverManager, o By.
import pytest 
from pages.login_page import LoginPage 

def test_login_simple(driver):

    login = LoginPage(driver)
    login.abrir()
    login.completar_usuario('standard_user')
    login.completar_clave('secret_sauce')
    login.hacer_clic_login()
    
    # La aserción final se mantiene en el test
    assert "/inventory.html" in driver.current_url
    assert "Swag Labs" in driver.title


def test_catalogo_valido(login_exitoso):
    catalogo = login_exitoso
    
    # Validaciones usando métodos de la página (POM)
    assert catalogo.obtener_titulo() == "Products"
    assert catalogo.contar_productos() > 0
    
    nombre, precio = catalogo.obtener_primer_producto()
    assert len(nombre) > 0
    assert precio.startswith("$")


def test_agregar_producto_y_navegar_a_carrito(login_exitoso):
 
    catalogo = login_exitoso # type: ignore

    # Acciones de alto nivel
    nombre_producto_agregado = catalogo.agregar_primer_producto_al_carrito()

    # La navegación retorna la siguiente Page Object (CartPage)
    carrito = catalogo.navegar_a_carrito()

    # Validaciones en la nueva página
    assert carrito.verificar_producto_por_nombre(nombre_producto_agregado)