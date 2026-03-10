import requests
import os
from dotenv import load_dotenv
load_dotenv()
# ----------------------------------------------------------
#  CONFIGURACIÓN: reemplazar TU_API_KEY con la que COPIAROOOOOOOOOOOOOOOON IMPORTANTISIMO
# ----------------------------------------------------------
API_KEY = os.getenv("APIKEY")
 
# Pedir ciudad al usuario
ciudad = input("\n Ingrese una ciudad: ")
 
# Construir la URL de la API
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
        
 
# Hacer la petición HTTP a OpenWeather
print("\nConsultando datos del clima...")
respuesta = requests.get(url)
 
# Verificar que la petición fue exitosa
if respuesta.status_code != 200:
    print(f"\n Error {respuesta.status_code}: ciudad no encontrada")
    exit()
 
# Convertir la respuesta JSON a un diccionario Python
datos = respuesta.json()
 
# Extraer los datos que necesitamos
temp       = datos["main"]["temp"]
humedad    = datos["main"]["humidity"]
descripcion= datos["weather"][0]["description"]
lat        = datos["coord"]["lat"]
lon        = datos["coord"]["lon"]
sensacion  = datos["main"]["feels_like"]
viento     = datos["wind"]["speed"]
 
# Mostrar resultados de forma bonita
print("\n" + "═" * 45)
print(f"  CLIMA EN {ciudad.upper()}")
print("═" * 45)
print(f"Temperatura    : {temp} °C")
print(f"Sensación térm.: {sensacion} °C")
print(f"Humedad        : {humedad}%")
print(f"Viento         : {viento} m/s")
print(f"Descripción    : {descripcion}")
print(f"Coordenadas    : {lat}, {lon}")
print("═" * 45)


import folium
 
# Crear el mapa centrado en las coordenadas de la ciudad
mapa = folium.Map(
    location=[lat, lon],
    zoom_start=12,
    tiles="OpenStreetMap"
)
 
# Crear un popup con información del clima
popup_texto = f"""
    <div style='font-family:Arial; font-size:14px; padding:8px'>
        <b>{ciudad}</b><br>
        Temperatura: {temp} °C<br>
        Humedad: {humedad}%<br>
        {descripcion}
    </div>
"""
 
# Agregar marcador con el popup
folium.Marker(
    location=[lat, lon],
    popup=folium.Popup(popup_texto, max_width=250),
    tooltip=f"{ciudad} — Click para ver clima",
    icon=folium.Icon(color="blue", icon="cloud", prefix="fa")
).add_to(mapa)
 
# Agregar un círculo para marcar el área
folium.Circle(
    location=[lat, lon],
    radius=5000,
    color="#2563EB",
    fill=True,
    fill_opacity=0.1
).add_to(mapa)
 
# Guardar el mapa como HTML
mapa.save("mapa_clima.html")
print("\n ¡Mapa generado! Abrir el archivo mapa_clima.html en tu navegador.")
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime
 
# Cargar las credenciales desde el archivo JSON descargado
cred = credentials.Certificate("clave.json")
firebase_admin.initialize_app(cred)
 
# Conectar con Firestore
db = firestore.client()
 
# Crear el documento con los datos de la consulta
consulta = {
    "ciudad":      ciudad,
    "temperatura": temp,
    "humedad":     humedad,
    "descripcion": descripcion,
    "viento_ms":   viento,
    "latitud":     lat,
    "longitud":    lon,
    "timestamp":   datetime.datetime.now().isoformat()
}
 
# Guardar en la colección 'consultas_clima'
db.collection("consultas_clima").add(consulta)
print("\n Consulta guardada en Firebase Firestore.")
print("   Ir a la consola de Firebase para verla en tiempo real.")
