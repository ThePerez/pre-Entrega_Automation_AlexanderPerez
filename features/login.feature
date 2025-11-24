Feature: Autenticación de Usuarios en Sauce Labs
  Como usuario de Sauce Labs, quiero poder iniciar sesión
  Para acceder al inventario de productos.

  Background: Abrir la página de autenticación
    Given estoy en la página de login

  @smoke @ui
  Scenario: 1. Inicio de sesión exitoso con credenciales válidas
    When ingreso el usuario "standard_user" y la clave "secret_sauce"

    Then debo ser redirigido a la página de inventario
    And veo el título "Products"


  @regression @error @ui
  Scenario Outline: 2. Intentos de inicio de sesión fallidos
    When ingreso el usuario "<usuario>" y la clave "<clave>"

    Then permanezco en la página de login
    And veo el mensaje de error "<mensaje_error>"

    Examples:
      | usuario           | clave          | mensaje_error                                                            |
      | user_invalido     | clave_invalida | Epic sadface: Username and password do not match any user in this service  |
      | locked_out_user   | secret_sauce   | Epic sadface: Sorry, this user has been locked out.                      |
      | standard_user     |                | Epic sadface: Password is required                                       |
      |                   | secret_sauce   | Epic sadface: Username is required                                       |