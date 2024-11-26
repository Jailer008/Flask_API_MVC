from selenium import webdriver
from selenium.webdriver.common.by import By


def test_user_name_display(user_id,name):
    # Configurar el WebDriver
    driver = webdriver.Chrome()

    try:
        # URL del usuario en la interfaz web
        url = f"http://127.0.0.1:5001/users/get_user_data/{user_id}"

        # Navegar a la URL
        driver.get(url)

        # Esperar a que el elemento del nombre de usuario aparezca en la página
        user_name_element = driver.find_element(By.CLASS_NAME,
                                                'name')  # Usa el localizador adecuado, como el class name

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