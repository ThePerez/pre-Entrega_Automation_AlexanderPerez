import requests
import pytest
from utils.api_utils import APIUtils

def test_get_users_structure():
    """
    Valida GET /users y la estructura de datos.
    Requisito PDF Pág 13: Verificar claves id, email, etc.
    """
    response = requests.get(APIUtils.USERS_ENDPOINT)
    
    # 1. Validar Status Code
    assert response.status_code == 200, f"Falló con {response.status_code}"
    
    data = response.json()
    assert len(data) > 0, "La lista de usuarios está vacía"
    
    # 2. Validar estructura del primer usuario
    user = data[0]
    assert "id" in user
    assert "email" in user
    assert "name" in user # JSONPlaceholder usa 'name' en vez de first_name
    
    print(f"\nUsuario validado: {user['name']} ({user['email']})")