import requests
import pytest

# URL para listar usuarios (Página 2)
URL = 'https://reqres.in/api/users?page=2'

def test_get_users():
    """
    Prueba GET: Listar usuarios
    1. Envía solicitud GET.
    2. Valida status 200.
    3. Valida que recibimos la página 2.
    4. Valida que la lista de datos no esté vacía.
    """
    
    # Usamos un User-Agent simple por si acaso
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # 1. Enviamos la solicitud GET
    r = requests.get(URL, headers=headers)
    
    # 2. Validamos el código de estado
    assert r.status_code == 200, f"Error: Se obtuvo {r.status_code}"
    
    # 3. Obtenemos el JSON
    data = r.json()
    
    # 4. Validaciones lógicas según el PDF [cite: 100-101]
    # Validar que estamos en la página 2
    assert data['page'] == 2, "La página retornada no es la 2"
    
    # Validar que hay usuarios en la lista 'data'
    assert len(data['data']) > 0, "La lista de usuarios está vacía"
    
    # Validación extra de estructura (Nivel 3 del PDF [cite: 171])
    primer_usuario = data['data'][0]
    assert 'email' in primer_usuario
    assert 'first_name' in primer_usuario
    
    print(f"\nTest GET exitoso. Usuario encontrado: {primer_usuario['first_name']}")