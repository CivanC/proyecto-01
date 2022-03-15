from src import *
from threading import Thread

def run():
    """Función para hacer la prueba de cinco búsquedas de vuelos.

    Returns:
        DataFrame: Información climática del origen y destino de cinco vuelos ordenada en un dataframe para estética visual.
    """
    cache = dict()
    list_origin = []
    list_destination = []
    list = []

    for i in range(5):
        list.append(np.random.randint(0, 2999))
    print("Los vuelos buscados fueron: ", list[0], ", ", list[1], ", ", list[2], ", ", list[3], " y ", list[4], ".")

    for i in list:
        t1 = Thread(target=datum_origin, args=(i, data(), cache, list_origin))
        t2 = Thread(target=datum_destination, args=(i, data(), cache, list_destination))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    df_or = pd.DataFrame(list_origin, columns = ["Origen", "Temperatura actual", "Humedad actual", "Presión actual", "Clima actual"])
    df_des = pd.DataFrame(list_destination, columns = ["Destino", "Temperatura esperada", "Humedad esperada", "Presión esperada", "Clima esperado"])
    final = df_or.join(df_des)
    return(final)