FROM python:3.9-slim

WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir requests kafka-python

# Copiar el resto de la aplicación
COPY . .

# Comando para ejecutar el scrapper
CMD ["python", "scrapper.py"]
