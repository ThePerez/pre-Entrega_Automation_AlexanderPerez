import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage 

# Fixture del driver estándar para pytest-selenium
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless") # Descomenta si no quieres ver el navegador
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def login_exitoso(driver):
    login_page = LoginPage(driver)
    inventory_page = login_page.login_completo('standard_user', 'secret_sauce') 
    return inventory_page

# ESTA ES LA CLAVE: Hook simplificado que usa la librería nativa
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # Busca el driver en los fixtures
        driver = item.funcargs.get('driver')
        if not driver and 'login_exitoso' in item.funcargs:
             driver = item.funcargs['login_exitoso'].driver
        
        if driver:
            # Toma la foto en Base64 directamente (sin guardar archivo físico)
            screenshot = driver.get_screenshot_as_base64()
            # La incrusta en el HTML
            extra.append(pytest_html.extras.image(screenshot))
            
    report.extra = extra