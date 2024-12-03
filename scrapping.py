from bs4 import BeautifulSoup
import requests

def obtener_datos_trafico(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Ejemplo de extracción (debes adaptar según la estructura de Waze)
            incidentes = soup.find_all(class_="leaflet-pane leaflet-marker-pane")  # Nombre del selector hipotético
            for incidente in incidentes:
                tipo = incidente.find(class_="incident-type").text
                ubicacion = incidente.find(class_="location").text
                severidad = incidente.find(class_="severity").text
                print(f"Incidente: {tipo}, Ubicación: {ubicacion}, Severidad: {severidad}")
        else:
            print("Error en la solicitud:", response.status_code)
    except Exception as e:
        print("Error al obtener datos:", e)

# Llamada al scrapper
obtener_datos_trafico("https://www.waze.com/es-419/live-map")
