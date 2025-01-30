import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    os.makedirs("logs", exist_ok=True)

    # Verifica si estás en un contenedor Docker
    is_docker = os.path.exists('/.dockerenv')

    # Define el host según el entorno
    host = '0.0.0.0' if is_docker else '127.0.0.1'
    port = 5000

    app.run(host=host, port=port)

