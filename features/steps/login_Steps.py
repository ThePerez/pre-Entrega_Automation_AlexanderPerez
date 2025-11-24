from behave import given, when, then
from pages.login_page import LoginPage         
from pages.inventory_page import InventoryPage
import logging

logger = logging.getLogger('behave') 

@given('estoy en la página de login')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    logger.info("Navegando a la página de login.")


@when('ingreso el usuario "{user}" y la clave "{password}"')
def step_impl(context, user, password):
    context.login_page.login(user, password)
    logger.info(f"Intentando loggear con usuario: {user}")


@then('debo ser redirigido a la página de inventario')
def step_impl(context):
    context.inventory_page = InventoryPage(context.driver)
    context.inventory_page.verify_url()
    logger.info("Verificación: Redirección exitosa a inventario.")


@then('veo el título "{title}"')
def step_impl(context, title):
    assert context.inventory_page.get_title_text() == title
    logger.info(f"Validación: Título de página verificado: {title}")


@then('veo el mensaje de error "{error_message}"')
def step_impl(context, error_message):
    assert context.login_page.is_error_message_visible(), "El mensaje de error no se mostró."
    actual_text = context.login_page.get_error_message_text()
    assert actual_text == error_message, f"Texto de error incorrecto. Esperado: '{error_message}', Obtenido: '{actual_text}'"
    logger.info(f"Validación: Mensaje de error verificado.")


@then('permanezco en la página de login')
def step_impl(context):
    current_url = context.driver.current_url
    assert "index.html" in current_url or "saucedemo.com" in current_url
    logger.info("Validación: Permaneció en la página de login.")