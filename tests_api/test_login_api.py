import requests
import pytest

# Usamos Restful-Booker que es amigable para testing de Login
LOGIN_URL = 'https://restful-booker.herokuapp.com/auth'

def test_login_exitoso():
 
    # Credenciales por defecto de esta API
    payload = {
        "username": "admin",
        "password": "password123"
    }
    
    headers = {"Content-Type": "application/json"}
    
    # Enviamos POST
    response = requests.post(LOGIN_URL, json=payload, headers=headers)
    
    # 1. Validar Status 200
    assert response.status_code == 200, f"Error: Se esperaba 200, se obtuvo {response.status_code}"
    
    # 2. Validar Token
    data = response.json()
    assert "token" in data, "La respuesta no trajo el token esperado"
    
    print(f"\nLogin OK! Token generado: {data['token']}")