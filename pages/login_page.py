from selenium.webdriver.common.by import By

class LoginPage:
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    #LOCATOR para el error (visto en los requerimientos)
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'h3[data-test="error"]')
    
    def __init__(self, driver, url="https://www.saucedemo.com/"):
        self.driver = driver
        self.url = url
        
    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # AÑADIR MÉTODOS DE VALIDACIÓN DE ERRORES.
    def is_error_message_visible(self):
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).is_displayed()
        except:
            return False

    def get_error_message_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text