import requests

def read_k8s_url():
    """
    Lee la URL del archivo k8s_url.txt.
    """
    try:
        with open("k8s_url.txt", "r") as file:
            url = file.read().strip()
            print(f"URL leída desde k8s_url.txt: {url}")
            return url
    except FileNotFoundError:
        print("Error: El archivo k8s_url.txt no existe.")
        return None

def test_backend(url):
    """
    Realiza una prueba HTTP GET a la API desplegada en Kubernetes.
    """
    if not url:
        print("Error: No se pudo obtener la URL.")
        return

    # Endpoint de prueba (ajusta según tu API)
    endpoint = "/users/1"  # Por ejemplo, para probar un endpoint de usuarios
    full_url = f"{url}{endpoint}"

    print(f"Probando la API en: {full_url}")

    try:
        response = requests.get(full_url)
        print(f"Respuesta de la API: Código de estado {response.status_code}")

        if response.status_code == 200:
            print("¡Prueba exitosa! La API respondió correctamente.")
            print("Respuesta JSON:", response.json())  # Si la API devuelve JSON
        else:
            print(f"Error: La API respondió con un código de estado {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud HTTP: {e}")

if __name__ == "__main__":
    # Lee la URL del archivo k8s_url.txt
    k8s_url = read_k8s_url()

    # Realiza la prueba en la API
    test_backend(k8s_url)