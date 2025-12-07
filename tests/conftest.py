import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage 


@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(5)
    
    yield driver
    
    driver.quit()


@pytest.fixture
def login_exitoso(driver):
    login_page = LoginPage(driver)
    
    # login_completo manejará internamente la importación de CatalogPage
    catalog_page = login_page.login_completo('standard_user', 'secret_sauce')
    
    return catalog_page