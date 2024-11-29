from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_user_name_display(user_id,name):

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ejecuta en modo headless
    chrome_options.add_argument("--disable-gpu")  # Optimización para ciertos sistemas
    chrome_options.add_argument("--no-sandbox")  # Necesario en algunos entornos
    chrome_options.add_argument("--disable-dev-shm-usage")  # Manejo de memoria compartida

    # Configurar el WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # URL del usuario en la interfaz web

        url = f"http://127.0.0.1:5001/users/get_user_data/{user_id}"

        # Navegar a la URL
        driver.get(url)

        wait = WebDriverWait(driver, 2)  # Tiempo máximo de espera: 10 segundos
        user_name_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'name')))

        # Verificar que el elemento se muestra
        if user_name_element.is_displayed():
            print("El nombre de usuario está presente en la interfaz.")
            if name == user_name_element.text :
                print("El nombre de usuario coincide con el testing")
                print("El nombre de usuario es: ", user_name_element.text)
            else:
                print("El nombre de usuario no coincide con el testing")

        else:
            print("El nombre de usuario no está visible en la interfaz.")

    except Exception as e:
        print("Error durante la prueba:", e)
    finally:
        # Cerrar la sesión del navegador
        driver.quit()


# Ejecutar la prueba con un ID de usuario existente
test_user_name_display(2200,"Leticia Herrera Estrada")  # Reemplaza 1 con un ID de usuario válido