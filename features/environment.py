import logging
from selenium import webdriver
from behave import fixture, use_fixture
import os

logger = logging.getLogger('behave')

@fixture
def selenium_browser_init(context):
    # before_all(): Configurar WebDriver una vez
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10) 
    logger.info("WebDriver inicializado.")
    yield context.driver
    # after_all(): Cerrar WebDriver y limpiar recursos
    context.driver.quit()
    logger.info("WebDriver cerrado.")


def before_all(context):
    use_fixture(selenium_browser_init, context)
  
    context.screenshot_dir = os.path.join(os.getcwd(), 'reports', 'screenshots')
    os.makedirs(context.screenshot_dir, exist_ok=True)
    logger.info("Ejecución de suite BDD iniciada.")


def after_step(context, step):

    # after_step(): Capturar screenshot automático en fallos
    if step.status == "failed":
        # Generar un nombre descriptivo para el archivo
        screenshot_name = f"{context.scenario.name.replace(' ', '_')}_{step.name.replace(' ', '_')}.png"
        screenshot_path = os.path.join(context.screenshot_dir, screenshot_name)
        
        # Capturar la pantalla
        context.driver.save_screenshot(screenshot_path)
        logger.error(f"Captura de pantalla guardada en: {screenshot_path}")


def after_all(context):
    logger.info("Ejecución de suite BDD finalizada.")