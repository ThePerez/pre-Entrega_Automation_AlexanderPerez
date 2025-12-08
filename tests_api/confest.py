import pytest

# Definimos la URL base una sola vez (JSONPlaceholder)
BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope='module')
def posts_url():
    """Fixture que devuelve la URL para colección de posts"""
    return f"{BASE_URL}/posts"

@pytest.fixture(scope='module')
def post_by_id_url():
    """Fixture factory que devuelve una función para generar URLs por ID"""
    def _get_url(post_id):
        return f"{BASE_URL}/posts/{post_id}"
    return _get_url