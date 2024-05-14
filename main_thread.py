import PyPDF2
import re
import threading
import queue
import time


def data_clean(text):
    NoNumbers = "".join([i for i in text if not i.isdigit()])  # Elimina números
    NoNumbers = text.lower()  # Convierte el texto en minusculas
    onlyText = re.sub(r"[-z\s]+", " ", NoNumbers)  # Eliminar puntuación
    finaltext = "".join(
        [s for s in onlyText.strip().splitlines(True) if s.strip()]
    )  # Elimina espacios nulos
    return finaltext


def splitlines(text, n, bandera):
    linessplit = text.split()  # Divide las líneas en una lista

    if bandera == 1:
        split = linessplit[
            0:n
        ]  # Crea la primera división con el primer número "a" de líneas en la división 1
    else:
        split = linessplit[
            n:
        ]  # Crea la primera división con el primer número "a" de líneas en la división 2
    return split


def mapper_thread(text, queue):
    keyval = []
    for i in text:
        i = re.sub(r"[,\.\:]", "", i)
        keyval.append([i, 1])  # Crea diccionario [palabra,1]
    queue.put(keyval)


def sortedlists(list1, list2):
    out = list1 + list2  # Concatena listas
    out.sort(key=lambda x: x[0])  # Organiza palabras en orden alfabético
    return out


def partition(sorted_list):
    sort1out = []
    sort2out = []
    for i in sorted_list:
        if i[0] < "n":
            sort1out.append(i)  # Palabras que comienzan con letras antes que n
        else:
            sort2out.append(i)  # Palabras que van desepués de n
    return sort1out, sort2out


def reducer_thread(part_out1, queue):
    sum_reduced = []
    count = 1
    for i in range(0, int(len(part_out1))):
        if i < int(len(part_out1)) - 1:
            if part_out1[i] == part_out1[i + 1]:
                count = count + 1  # Cuenta el número de apariciones de la palabra
            else:
                sum_reduced.append(
                    [part_out1[i][0], count]
                )  # Agrega al diccionario la palabra y el número de apariciones
                count = 1
        else:
            sum_reduced.append(part_out1[i])  # Agrega la última palabra
    queue.put(sum_reduced)


def thread_(func, list1, list2):  # Crea hilos para map y reduce

    myQue1 = queue.Queue()  # Objetos para manejo de información con hilos
    myQue2 = queue.Queue()

    thread1 = threading.Thread(
        target=func,
        args=(
            list1,
            myQue1,
        ),
    )
    thread2 = threading.Thread(
        target=func,
        args=(
            list2,
            myQue2,
        ),
    )
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    list1 = myQue1.get()
    list2 = myQue2.get()

    return list1, list2


if __name__ == "__main__":

    nombreFile = input("Ingrese nombre del archivo\n>")
    nombreFile = nombreFile + ".pdf"

    ini = time.time()  # Tiempo inicio

    try:
        File = open(nombreFile, "rb")

    except FileNotFoundError:
        print("EL ARCHIVO QUE INTENTA ABRIR NO EXISTE")

    else:
        data = PyPDF2.PdfReader(File)
        texto = ""

        for i in range(0, len(data.pages)):
            page = data.pages[i]
            texto = texto + page.extract_text()

        cleanData = data_clean(texto)

        lineaSplits1 = splitlines(cleanData, int(len(cleanData) / 2), 1)

        lineaSplits2 = splitlines(cleanData, int(len(cleanData) / 2), 2)

        mapp = thread_(mapper_thread, lineaSplits1, lineaSplits2)

        sortPalabra = sortedlists(mapp[0], mapp[1])

        slicePalabra = partition(sortPalabra)

        reducer = thread_(reducer_thread, slicePalabra[0], slicePalabra[1])

        outPalabra = reducer[0] + reducer[1]

        fin = time.time()  # Tiempo final

        for i in range(0, len(outPalabra)):
            print(outPalabra[i])

        print("\nTiempo de ejecucion: ", "{0:.4f}".format(fin - ini))
