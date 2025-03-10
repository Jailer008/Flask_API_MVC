import pytest
import requests
import random
from app.db import get_db_connection
from app.config import Config

table = f"{Config.DB_NAME}.users"

def test_new_user():
    # Generar valores para id_user y name_user
    id_user = str(random.randint(100, 999))
    name_user = "Test_" + id_user

    url = f"http://127.0.0.1:5000/users/{id_user}"
    headers = {"Content-Type": "application/json"}
    data = {"user_name": name_user}

    # Intentar realizar la solicitud POST
    try:
        post_response = requests.post(url, headers=headers, json=data)
        post_response.raise_for_status()
        print(f"Usuario {name_user} registrado con éxito en la API.")
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error al registrar usuario: {e}")

    # Intentar realizar la solicitud GET para verificar si el usuario se ha guardado
    try:
        get_response = requests.get(url)
        get_response.raise_for_status()
        response_data = get_response.json()
        assert response_data.get("user_name") == name_user, "El nombre de usuario devuelto no coincide."
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Error al obtener usuario: {e}")

    # Intentar conectarse a la base de datos y verificar si el usuario se ha guardado correctamente
    try:
        connection = get_db_connection()
        with connection:
            with connection.cursor() as cursor:
                query = f"SELECT name FROM {table} WHERE id = %s"
                cursor.execute(query, (id_user,))
                result = cursor.fetchone()
                assert result and result[0] == name_user, "Error: El usuario no se encontró en la base de datos."
    except Exception as e:
        pytest.fail(f"Error al consultar la base de datos: {e}")