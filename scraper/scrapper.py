import requests
import json
from kafka import KafkaProducer
import time

# Configuración de Kafka
KAFKA_BROKER = 'kafka:9092'
KAFKA_TOPIC = 'waze-alerts'

# Inicializar el productor de Kafka
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# URL del API de Waze
url = 'https://www.waze.com/live-map/api/georss?top=-33.318727734058896&bottom=-33.646196973860725&left=-70.77952194213869&right=-70.502254486084&env=row&types=alerts,traffic'

def fetch_and_send():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            alerts = data.get("alerts", [])
            for alert in alerts:
                producer.send(KAFKA_TOPIC, alert)
                print(f"Enviado alerta: {alert}")
        else:
            print(f"Error al acceder a la API. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error durante la solicitud o envío: {e}")

if __name__ == "__main__":
    while True:
        fetch_and_send()
        time.sleep(900)  # Intervalo de 15 minuto
