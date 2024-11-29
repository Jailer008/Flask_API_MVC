import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.config import Config
from app.db import get_db_connection


def combined_testing(id_user, name_user):
    # URL y cabeceras
    api_url = f"http://127.0.0.1:5000/users/{id_user}"
    web_url = f"http://127.0.0.1:5001/users/get_user_data/{id_user}"
    headers = {"Content-Type": "application/json"}
    data = {"user_name": name_user}

    # Paso 1: Enviar los datos de usuario con POST a la API REST
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code != 200:
        raise Exception("Test failed: Error en POST request.")

    # Paso 2: Realizar GET para verificar que los datos coinciden con lo enviado
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception("Test failed: Error en GET request.")

    response_data = response.json()
    if response_data.get("user_name") != name_user:
        raise Exception("Test failed: El nombre de usuario no coincide después del GET.")

    # Paso 3: Verificar que los datos se guardaron en la base de datos usando pymysql
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            query = f"SELECT name FROM {Config.DB_NAME}.users WHERE id = %s"
            cursor.execute(query, (id_user,))
            result = cursor.fetchone()
            if not result or result[0] != name_user:
                raise Exception("Test failed: Los datos en la base de datos no coinciden.")
    finally:
        connection.close()

    # Paso 4: Iniciar sesión de Selenium WebDriver y verificar el nombre de usuario en la interfaz web
    driver = webdriver.Chrome()
    driver.get(web_url)

    try:
        # Localizar el elemento que muestra el nombre de usuario
        user_name_element = driver.find_element(By.CLASS_NAME, "name")  # Asegúrate de que la clase coincide con el HTML
        if user_name_element.text != name_user:
            raise Exception("Test failed: El nombre de usuario en la interfaz web no coincide.")
        print("Test passed: Todos los datos son correctos.")
    finally:
        driver.quit()


# Prueba del script
combined_testing("2288", "ZCoin8")


