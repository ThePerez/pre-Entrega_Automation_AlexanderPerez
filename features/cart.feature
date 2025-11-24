Feature: Funcionalidad de Carrito de Compras
  Como usuario quiero añadir productos a mi carrito
  Para verificar que el contador se actualiza correctamente

  @regression @ui
  Background: Login con usuario estándar
    Given estoy en la página de login
    When ingreso el usuario "standard_user" y la clave "secret_sauce"
    Then debo ser redirigido a la página de inventario

  @regression @smoke @ui
  Scenario: 1. Agregar un solo producto al carrito
    When agrego el producto "Sauce Labs Backpack" al carrito
    Then el ícono del carrito debe mostrar el contador "1"
    
  @regression @ui
  Scenario: 2. Agregar múltiples productos al carrito
    When agrego el producto "Sauce Labs Bike Light" al carrito
    And agrego el producto "Sauce Labs Bolt T-Shirt" al carrito
    Then el ícono del carrito debe mostrar el contador "2"