from src import *
from threading import Thread

def run():
    cache = dict()
    list_origin = []
    list_destination = []
    list = []

    #for i in range(1500):
    for i in range(5):
        #list.append(i)
        list.append(np.random.randint(0, 2999))
    print("Los vuelos buscados fueron:")
    for i in list:
        print(i)

    #t1 = Thread(target=datum_origin, cache, list_origin)
    #t2 = Thread(target=datum_destination, cache, list_destination)

    for i in list:
        #t1 = Thread(target=datum_origin, args=[i, cache, list_origin])
        #t2 = Thread(target=datum_destination,args=[i,  cache, list_destination])
        #datum_origin(i, cache, list_origin)
        #datum_destination(i, cache, list_destination)
        t1 = Thread(target=datum_origin, args=(i, cache, list_origin))
        t2 = Thread(target=datum_destination, args=(i,  cache, list_destination))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    df_or = pd.DataFrame(list_origin, columns = ["Origen", "Temperatura actual", "Humedad actual", "Presión actual", "Clima actual"])
    df_des = pd.DataFrame(list_destination, columns = ["Destino", "Temperatura esperada", "Humedad esperada", "Presión esperada", "Clima esperado"])
    final = df_or.join(df_des)
    return(final)