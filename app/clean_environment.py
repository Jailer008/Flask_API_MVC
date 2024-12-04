import requests

def finish_server():
    try:
        requests.get('http://127.0.0.1:5001/stop_server')
    except requests.exceptions.RequestException as e:
        print(f"Se produjo un error al realizar la solicitud en backend: {e}")

    try:
        requests.get('http://127.0.0.1:5000/stop_server')
    except requests.exceptions.RequestException as e:
        print(f"Se produjo un error al realizar la solicitud en frontend: {e}")

finish_server()