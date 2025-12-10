import pytest 
from pages.login_page import LoginPage 
from pages.checkout_information_page import CheckoutInformationPage # Necesaria para el nuevo test

# --- TEST PARAMETRIZADO DE LOGIN ---
@pytest.mark.parametrize(
    "usuario, clave, url_esperada, error_esperado", 
    [
        ("standard_user", "secret_sauce", "inventory.html", None), # Éxito
        ("locked_out_user", "secret_sauce", None, "Epic sadface: Sorry, this user has been locked out."), # Bloqueado
        ("usuario_invalido", "clave_invalida", None, "Epic sadface: Username and password do not match any user in this service"), # Inválido
    ]
)
def test_login_parametrizado(driver, usuario, clave, url_esperada, error_esperado):
    login = LoginPage(driver)
    
    login.abrir().completar_usuario(usuario).completar_clave(clave).hacer_clic_login()
    
    if error_esperado:
        assert login.esta_error_visible()
        assert login.obtener_mensaje_error() == error_esperado
    else:
        assert url_esperada in driver.current_url
        assert not login.esta_error_visible()


# --- TESTS DE FLUJO ---

def test_catalogo_valido(login_exitoso):
    catalogo = login_exitoso
    
    assert catalogo.obtener_titulo() == "Products"
    assert catalogo.contar_productos() > 0
    
    nombre, precio = catalogo.obtener_primer_producto()
    assert len(nombre) > 0
    assert precio.startswith("$")


def test_agregar_producto_y_navegar_a_carrito(login_exitoso):
    catalogo = login_exitoso

    nombre_producto_agregado = catalogo.agregar_primer_producto_al_carrito()
    carrito = catalogo.navegar_a_carrito()

    assert carrito.verificar_producto_por_nombre(nombre_producto_agregado)


def test_flujo_compra_completa(login_exitoso):
    catalogo = login_exitoso

    # 1. Agregar Producto y Navegar al Carrito
    nombre_producto = catalogo.agregar_primer_producto_al_carrito()
    carrito = catalogo.navegar_a_carrito() 

    # 2. Iniciar Checkout (CartPage -> InfoPage)
    info_page = carrito.iniciar_checkout()

    # 3. Llenar Información y Continuar (InfoPage -> OverviewPage)
    overview_page = info_page.completar_informacion("Alexander", "Perez", "1000") \
                            .continuar_a_overview()

    # 4. Validar Resumen de la Orden
    assert overview_page.obtener_nombre_producto() == nombre_producto
    
    # 5. Finalizar Compra (OverviewPage -> CompletePage)
    confirmacion_page = overview_page.finalizar_compra()

    # 6. Validar Éxito
    assert confirmacion_page.es_pagina_de_confirmacion()
  
  # FORZAMOS EL FALLO para probar el screenshot
  #  assert False, "PRUEBA DE SCREENSHOT: Fallo forzado para verificar el reporte"