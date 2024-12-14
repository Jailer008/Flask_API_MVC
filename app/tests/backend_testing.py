import requests
from app.db import get_db_connection
from app.config import Config

table = f"{Config.DB_NAME}.users"

def test_new_user(id_user, name_user):
    url = f"http://127.0.0.1:5000/users/{id_user}"
    headers = {"Content-Type": "application/json"}
    data = {"user_name": name_user}

    # Intentar realizar la solicitud POST
    try:
        post_response = requests.post(url, headers=headers, json=data)
        post_response.raise_for_status()  # Verifica si el código de estado indica error
        print(f"Usuario {name_user} registrado con éxito en la API.")
    except requests.exceptions.RequestException as e:
        print(f"Error al registrar usuario: {e}")
        return  # Salir si falla el POST

    # Intentar realizar la solicitud GET para verificar si el usuario se ha guardado
    try:
        get_response = requests.get(url)
        get_response.raise_for_status()
        response_data = get_response.json()
        if response_data.get("user_name") == name_user:
            print("Usuario registrado correctamente:", name_user)
        else:
            print("El nombre de usuario devuelto no coincide.")
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener usuario: {e}")
        return  # Salir si falla el GET

    # Intentar conectarse a la base de datos y verificar si el usuario se ha guardado correctamente
    try:
        connection = get_db_connection()
        with connection:
            with connection.cursor() as cursor:
                query = f"SELECT name FROM {table} WHERE id = %s"
                cursor.execute(query, (id_user,))
                result = cursor.fetchone()
                if result and result[0] == name_user:
                    print("User ID is saved under:", name_user)
                else:
                    print("Error: El usuario no se encontró en la base de datos.")
    except Exception as e:
        print(f"Error al consultar la base de datos: {e}")

# Prueba de la función
test_new_user("5565", "Test_565")

