import requests
import pytest
import time

@pytest.mark.api
@pytest.mark.e2e
def test_ciclo_vida_post_completo(posts_url, post_by_id_url):

    # --- PASO 1: CREAR (POST) ---
    payload_creacion = {
        "title": "Post creado por Alexander QA",
        "body": "Este es un post de prueba para el ciclo de vida",
        "userId": 1
    }
    
    # Medimos tiempo de respuesta (Requisito: < 3s)
    start_time = time.time()
    resp_post = requests.post(posts_url, json=payload_creacion)
    total_time = time.time() - start_time
    
    # Validaciones POST
    assert resp_post.status_code == 201, "El POST no devolvió 201 Created"
    data_created = resp_post.json()
    new_id = data_created['id']
    print(f"\n1. POST: Recurso creado con ID: {new_id} (Tiempo: {total_time:.2f}s)")
    
    assert total_time < 3.0, "El POST tardó demasiado"
  
    target_id = 1 
    url_patch = post_by_id_url(target_id)
    
    payload_update = {
        "title": "Titulo ACTUALIZADO por Alexander QA"
    }
    
    resp_patch = requests.patch(url_patch, json=payload_update)
    
    # Validaciones PATCH
    assert resp_patch.status_code == 200, "El PATCH no devolvió 200 OK"
    data_updated = resp_patch.json()
    
    # Validar que el título cambió
    assert data_updated['title'] == payload_update['title'], "El título no se actualizó correctamente"
    print(f"2. PATCH: Título actualizado correctamente en ID {target_id}")

    # --- PASO 3: ELIMINAR (DELETE) ---
    url_delete = post_by_id_url(target_id)
    resp_delete = requests.delete(url_delete)
    
    # Validaciones DELETE
    assert resp_delete.status_code == 200, "El DELETE no devolvió 200 OK"
    # JSONPlaceholder devuelve {} al borrar
    assert resp_delete.json() == {}, "El cuerpo de respuesta DELETE no está vacío"
    print(f"3. DELETE: Recurso eliminado correctamente")

    print("\n✅ Ciclo de vida completo validado exitosamente.")