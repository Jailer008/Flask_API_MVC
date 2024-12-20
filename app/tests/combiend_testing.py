import requests
from app.config import Config
from app.db import get_db_connection
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

def combined_testing(id_user, name_user):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # Ejecuta en modo headless
    chrome_options.add_argument("--disable-gpu")  # Optimización para ciertos sistemas
    chrome_options.add_argument("--no-sandbox")  # Necesario en algunos entornos
    chrome_options.add_argument("--disable-dev-shm-usage")  # Manejo de memoria compartida
    service = Service("/home/jailer/.jenkins/workspace/HereWeGo/bin/chromedriver")

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
    driver = webdriver.Chrome(options=chrome_options,service=service)
    driver.get(web_url)

    try:
        wait = WebDriverWait(driver, 2)  # Tiempo máximo de espera: 10 segundos
        user_name_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'name')))

        if user_name_element.text != name_user:
            raise Exception("Test failed: El nombre de usuario en la interfaz web no coincide.")
        print("Test passed: Todos los datos son correctos.")

    except Exception as e:
        raise Exception(f"Selenium failed: {e}")

    finally:
        driver.quit()


# Prueba del script
combined_testing("66", "ZCoin66")


