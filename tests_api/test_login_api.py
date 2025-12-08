import requests
import pytest

# URL base de la API de pruebas
LOGIN_URL = 'https://reqres.in/api/login'

def test_login_exitoso():
    """
    Prueba de login exitoso:
    1. Envía credenciales válidas.
    2. Valida status code 200.
    3. Valida que la respuesta contenga un token.
    """
    
    # 1. Definimos los datos (Payload)
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    
    # 2. 🔑 SOLUCIÓN MEJORADA: Simulamos TODAS las cabeceras de un navegador real
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Content-Type": "application/json"
    }
    
    # 3. Usamos 'Session' para gestionar mejor la conexión (como un navegador)
    session = requests.Session()
    
    # Enviamos la petición POST
    response = session.post(LOGIN_URL, json=payload, headers=headers)
    
    # Debug: Si vuelve a fallar, veremos qué pasó
    if response.status_code != 200:
        print(f"\nStatus Code: {response.status_code}")
        print(f"Error: {response.text[:200]}...") # Imprimimos solo el inicio para no llenar la pantalla
    
    # 4. Validaciones (Assertions)
    assert response.status_code == 200, f"Error: Se esperaba 200 pero se obtuvo {response.status_code}"
    
    # 5. Convertimos la respuesta a JSON y validamos
    data = response.json()
    assert "token" in data, "La respuesta no contiene el token de autenticación"
    print(f"\nLogin exitoso! Token recibido: {data['token']}")