# Tarea1_SDistribuidos

<h1>#MAP-REDUCE</h1>

MapReduce es un paradigma de procesamiento de datos caracterizado por dividirse en dos fases o pasos diferenciados: Map y Reduce. 
Estos subprocesos asociados a la tarea se ejecutan de manera distribuida, en diferentes nodos de procesamiento o esclavos. 
Para controlar y gestionar su ejecución, existe un proceso Master o Job Tracker. 
También es el encargado de aceptar los nuevos trabajos enviados al sistema por los clientes.

Este sistema de procesamiento se apoya en tecnologías de almacenamiento de datos distribuidas, en cuyos nodos se ejecutan estas operaciones de tipo map y reduce. 
El sistema de ficheros distribuido de Hadoop es HDFS (Hadoop Distributed File System), encargado de almacenar los ficheros divididos en bloques de datos. 
HDFS proporciona la división previa de los datos en bloques que necesita MapReduce para ejecutar. 
Los resultados del procesamiento se pueden almacenar en el mismo sistema de almacenamiento o bien en una base de datos o sistema externo.

<h1>Objetivo</h1>

Se buscó simular un MapReduce desde python, para contar el número de apariciones de cada palabra que aparecen en un determinado archivo. 
Los arcivos de entradas son PDFs (Redalyc o Wikipedia).
Parte del objetivo es simular el MapReduce con un solo hilo y con multiples hilos.

<h1>Funcionalidades </h1>

La funcion principal del ejercicio es el MapReduce, dentro de los script estan definidas como dos funciones.
los script estan desarrollado en base a un entorno virtual de python, esto quiere decir que si las librerias correspondientes 
usadas en el ejecicio no estan previamente instaladas se generara un error. dependera del usuario si descarga las librerias 
de manera local o virtual.



<h4>Autores</h4>
<h5>Julián López</h5>
<h5>Manuel Moreno</h5>



