import requests
from dotenv import load_dotenv
load_dotenv()
# ----------------------------------------------------------
#  CONFIGURACIÓN: reemplazar TU_API_KEY con la que COPIAROOOOOOOOOOOOOOOON IMPORTANTISIMO
# ----------------------------------------------------------
API_KEY = "$APIKEY"
 
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
