# Imagen base
FROM python:3.8-alpine

# Establecer directorio de trabajo
WORKDIR /app

# Copiar el resto de los archivos al contenedor
COPY . /app

RUN apk add --no-cache gcc musl-dev libffi-dev && \
    pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 5000

# Definir Volumen
VOLUME /app/logs

# Comando de inicio
CMD ["python3", "run.py"]
