from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com"
        # Localizadores (es mejor definirlos fuera del constructor o como constantes)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        
    def cargar_pagina(self):  # <--- MÉTODO FALTANTE (Agregado)
        """Navega a la URL de la página de login."""
        self.driver.get(self.url)

    def ingresar_usuario(self, username):
        """Ingresa el nombre de usuario."""
        self.driver.find_element(*self.username_input).send_keys(username)
        
    def ingresar_contrasenia(self, password):
        """Ingresa la contraseña."""
        self.driver.find_element(*self.password_input).send_keys(password)

    def hacer_login(self):
        """Hace clic en el botón de Login."""
        self.driver.find_element(*self.login_button).click()