from behave import when, then
from pages.inventory_page import InventoryPage
import logging

logger = logging.getLogger('behave')


@when('agrego el producto "{product_name}" al carrito')
def step_impl(context, product_name):

    if not hasattr(context, 'inventory_page'):
        context.inventory_page = InventoryPage(context.driver)
        
    context.inventory_page.add_item_to_cart(product_name)
    logger.info(f"Producto agregado al carrito: {product_name}")


@then('el ícono del carrito debe mostrar el contador "{expected_count}"')
def step_impl(context, expected_count):

    if not hasattr(context, 'inventory_page'):
        context.inventory_page = InventoryPage(context.driver)

    actual_count = context.inventory_page.get_cart_count()
    assert actual_count == expected_count, f"El contador esperado era '{expected_count}' pero se encontró '{actual_count}'."
    logger.info(f"Contador de carrito verificado: {actual_count}")