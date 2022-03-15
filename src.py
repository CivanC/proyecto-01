import requests, json
import pandas as pd
import numpy as np
import os

def data():
    """Función para leer los 3mil vuelos de entrada y convertirlos a un dataframe para su manejo.

    Returns:
        DataFrame: Dataframe con los datos requeridos
    """
    direct = os.path.dirname(__file__)
    data_direct = os.path.join(direct, "data\\dataset1.csv")
    return pd.read_csv(data_direct)

def tempC(x):
    """Función que convierte temperaturas Kelvin a grados Celsius.

    Args:
        x (integer): Temperatura en Kelvin a convertir.

    Returns:
        float: Temperatura en grados Celsius redondeada.
    """
    assert (x >= 0),"La temperatura es más fría que el cero absoluto; si vas ahí morirás."
    return round(x - 273.15, 1)

def new_data(num, x, data):
    """Función para buscar datos de un vuelo no obtenidos anteriormente. Se usó como
    referencia la página https://www.tutorialspoint.com/find-current-weather-of-any-city-using-openweathermap-api-in-python

    Args:
        num (integer): Índice obtenido por funciones anteriores para diferenciar si es localización origen o destino.
        x (integer): Índice del vuelo a buscar.
        data (DataFrame): Base de datos de los vuelos.

    Returns:
        list: Características climáticas del lugar buscado en una lista ordenada.
    """

    if num == 1:
        lat = str(data.origin_latitude[x])
        lon = str(data.origin_longitude[x])
    else:
        lat = str(data.destination_latitude[x])
        lon = str(data.destination_longitude[x])

    url = "https://api.openweathermap.org/data/2.5/weather?" + "lat=" + lat + "&lon=" + lon + "&appid=f54a7d5754bf89a7ffc87f9a66599730&lang=sp"
    response = requests.get(url)

    assert(response.status_code == 200),"Error en la petición HTTP."

    datu = response.json()
    main = datu["main"]
    tempK = main["temp"]
    temp = str(tempC(tempK)) + " °C"
    hum = str(main["humidity"]) + "%"
    pres = str(main["pressure"]) + " Pa"
    rep = datu["weather"]
    weath = rep[0]["description"]
    
    return [temp, hum, pres, weath]

def datum_origin(x, data, cache, list_origin):
    """Función para búsqueda de datos del lugar origen.

    Args:
        x (integer): El índice del vuelo a utilizar.
        data (DataFrame): Base de datos de los vuelos.
        cache (dictionary): Diccionario para usar como caché.
        list_origin (list): Lista para almacenar los datos conseguidos ordenadamente.

    Returns:
        list: Características climáticas del lugar de origen en una lista ordenada.
    """
    key = data.origin[x]

    if key not in cache:
        cache[key] = new_data(1, x, data)
    
    list_origin.append([key,cache[key][0],cache[key][1],cache[key][2],cache[key][3]])
    return cache[key]

def datum_destination(x, data, cache, list_destination):
    """Función para búsqueda de datos del lugar destino.

    Args:
        x (integer): El índice del vuelo a utilizar.
        data (DataFrame): Base de datos de los vuelos.
        cache (dictionary): Diccionario para usar como caché.
        list_origin (list): Lista para almacenar los datos conseguidos ordenadamente.

    Returns:
        list: Características climáticas del lugar destino en una lista ordenada.
    """

    key = data.destination[x]
    if key not in cache:
        cache[key] = new_data(666, x, data)
    list_destination.append([key,cache[key][0],cache[key][1],cache[key][2],cache[key][3]])
    return cache[key]