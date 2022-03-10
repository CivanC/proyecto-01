# %%
# Instalación de paquetería a utilizar: requests para conseguir información de OpenWeatherMap, pandas para leer y escribir archivos de extensión csv y numpy para la función random usada en las pruebas.
%pip install requests pandas numpy

# %%
# Importación y renombre de utilidades para mayor conveniencia.
import requests, json
import pandas as pd
import numpy as np

# %%
# Lectura de los datos a utilizar.
data = pd.read_csv("dataset1.csv")

# Visualización de los datos.
data

# %%
# Definición de funciones y estructuras a utilizar.

# Creación de cache por diccionario.
cache = dict()

# Creación de listas para ordenar los vuelos.
list_origin = []
list_destination = []

# Función para convertir Kelvin a grados Celsius.
def tempC(x):
    # Manejo de temperatura errónea.
    assert (x >= 0),"La temperatura es más fría que el cero absoluto; si vas ahí morirás."
    # Redondeo estético a un decimal.
    return round(x - 273.15, 1)

# Función para búsqueda de datos no obtenidos anteriormente.
# Se usó como referencia el código de https://www.tutorialspoint.com/find-current-weather-of-any-city-using-openweathermap-api-in-python
def new_data(num,x):
    # Identificación de origen o destino.
    if num == 1:
        lat = str(data.origin_latitude[x])
        lon = str(data.origin_longitude[x])
    else:
        lat = str(data.destination_latitude[x])
        lon = str(data.destination_longitude[x])

    # URL de la localización por latitud y longitud.
    url = "https://api.openweathermap.org/data/2.5/weather?" + "lat=" + lat + "&lon=" + lon + "&appid=f54a7d5754bf89a7ffc87f9a66599730&lang=sp"

    # Petición htlm.
    response = requests.get(url)

    # Manejo de errores por el código de estado de la petición.
    assert(response.status_code == 200),"Error en la petición HTTP."

    # Obtención de datos en formato json.
    datu = response.json()
    # Obtención de bloque de datos principal.
    main = datu["main"]
    # Obtención de temperatura.
    tempK = main["temp"]
    # Conversión de Kelvin a grados celsius.
    temp = str(tempC(tempK)) + " °C"
    # Obtención de humedad
    hum = str(main["humidity"]) + "%"
    # Obtención de presión
    pres = str(main["pressure"]) + " Pa"
    # Obtención del clima general.
    rep = datu["weather"]
    weath = rep[0]["description"]
    return [temp, hum, pres, weath]

# Función para búsqueda de datos del lugar origen.
def datum_origin(x):
    # Creación de llaves para el cache según el código IATA.
    key = data.origin[x]

    # Verificación de no haber encontrado los datos anteriormente.
    if key not in cache:
        # Guardado de datos en el cache.
        cache[key] = new_data(1,x)
    
    # Adición de datos a lista de localizaciones de origen ordenada.
    list_origin.append([key,cache[key][0],cache[key][1],cache[key][2],cache[key][3]])

    # Regreso de lista con los datos pertinentes.
    return cache[key]

# Función para búsqueda de datos del lugar destino.
def datum_destination(x):
    # Creación de llaves para el cache según el código IATA.
    key = data.destination[x]

    # Verificación de no haber encontrado los datos anteriormente.
    if key not in cache:
        # Guardado de datos en el cache.
        cache[key] = new_data(666,x)
    
    # Adición de datos a lista de localizaciones de origen ordenada.
    list_destination.append([key,cache[key][0],cache[key][1],cache[key][2],cache[key][3]])
    
    # Regreso de lista con los datos pertinentes.
    return cache[key]

# %%
# Construcción de cache y listas limpias.
cache = dict()
list_origin = []
list_destination = []

# Construcción de lista prueba.
list = []

# Iterador para conseguir muestra de distintos rangos.
for i in range(5):
    list.append(i+np.random.randint(0, 2997))
print(list)

# Llamada a funciones principales.
for i in list:
    datum_origin(i)
    datum_destination(i)

# %%
cache

# %%
# Guardado de resultados en dataframes individuales.

# Dataframe de lugares origen.
df_or = pd.DataFrame(list_origin, columns = ["Origen", "Temperatura actual", "Humedad actual", "Presión actual", "Clima actual"])

# Dataframe de lugares destino.
df_des = pd.DataFrame(list_destination, columns = ["Destino", "Temperatura esperada", "Humedad esperada", "Presión esperada", "Clima esperado"])

# Unión de dataframes final.
final = df_or.join(df_des)

# Visualización de prueba final.
final

# Convertir los resultados en formato csv.
final.to_csv('final.csv')


