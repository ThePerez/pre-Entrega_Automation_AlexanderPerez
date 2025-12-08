class APIUtils:
    # Usamos JSONPlaceholder para evitar el error 403 de Reqres
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    # Endpoints comunes
    USERS_ENDPOINT = f"{BASE_URL}/users"
    POSTS_ENDPOINT = f"{BASE_URL}/posts"