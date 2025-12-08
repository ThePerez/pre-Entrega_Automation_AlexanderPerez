import requests
import pytest
from utils.api_utils import APIUtils

# Datos de prueba parametrizados (Nombre, Trabajo/Título)
@pytest.mark.parametrize("nombre, trabajo", [
    ("Matias QA", "Tester Senior"),
    ("Alexander Dev", "Automation Lead"),
    ("Silvia PO", "Product Owner")
])
def test_create_user(nombre, trabajo):
    """
    Valida POST /users con parametrización.
    Requisito PDF Pág 13: Enviar POST con distintos nombres y validar 201.
    """
    payload = {
        "name": nombre,
        "job": trabajo  # JSONPlaceholder acepta cualquier campo extra
    }
    
    response = requests.post(APIUtils.USERS_ENDPOINT, json=payload)
    
    # Validaciones
    assert response.status_code == 201, f"Se esperaba 201, se obtuvo {response.status_code}"
    
    data = response.json()
    assert data['name'] == nombre
    assert 'id' in data
    
    print(f"\nUsuario creado: {data['name']} - ID asignado: {data['id']}")