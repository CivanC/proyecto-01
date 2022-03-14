Carlos Iván Canto Varela, 315649888
# proyecto-01

Web service para el clima de llegada y salida de 3000 tickets del aeropuerto de la Ciudad de México.

Se requiere un programa que informe del clima actual en la ciudad de partida y el clima esperado en la ciudad de llegada para 3 mil vuelos que se realizarán.

A primera instancia, mi primera idea fue realizar un scraper que visitara el sitio de Yahoo Weather, buscara las localizaciones según su código IATA y regresara el clima buscado. Después de hacer una pequeña prueba, descubrí que cada localización tardaba un promedio de 2 segundos de procesamiento, por lo que desistí en esa idea y decidí hacerlo con la API de OpenWeatherMap. Además se implementó un caché rústico por medio de diccionarios de Python para evitar llamadas innecesarias a la API.

El procedimiento para tratar los datos conseguidos fue crear un diccionario como caché. Luego, buscar las ciudades según su código IATA dentro del cache. Si no han sido buscadas dichas ciudades, se creará una entrada nueva en el diccionario con la clave IATA como su identificador y sus características climatológicas en una lista como el contenido de la entrada. Luego, cada ciudad buscada será añadida junto con sus características a una lista ordenada de origen o destino. Una vez hecho esto, se repetirá el proceso para cada ciudad de los 3 mil viajes.
Al finalizar el proceso, las listas de orígenes y llegadas serán convertidas a dataframes y se mezclarán como columnas para una visualización intuitiva.
Si me da tiempo, el proceso será optimizado mediante threading para ejecutar las búsquedas de origen y de llegada "simultáneamente". Si está leyendo esto, significa que aún no lo hago o no me dio tiempo de hacerlo.

En un futuro, si se decide expandir el servicio a más de 3 mil tickets o a búsquedas más frecuentes, la implementación podría verse insuficiente pues la licencia de estudiante sólo cubre 3 mil búsquedas por minuto. En este caso, el mantenimiento que deberá aplicarse dependerá del presupuesto disponible. Podría simplemente comprarse una licencia de mayor rango y cambiarse la llave de acceso, lo que tomaría unos minutos, cuando mucho. Mi costo sería el costo de la licencia y unas horas de salario mensualmente. En otro caso, lo que podría hacerse sería adaptar el código para correr 3 mil búsquedas cada minuto hasta cubrir las que son necesarias, lo que me podría llevar desde una hora hasta unos días. Por este servicio cobraría el doble. El salario a considerar sería el promedio de un Junior Developer por hora.
En un semestre, la llave utilizada para acceder a la API caducará y será necesario conseguir una nueva. Gracias a la implementación del código, el resultado que se visualizará será un error al encontrar los datos. Cuando esto pase y sea contactado (si no deciden utilizar a un tercero) cobraría por la licencia y un extra de $500 quizá.
