import PyPDF2
import re


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
        split1 = linessplit[
            0:n
        ]  # Crea la primera división con el primer número "a" de líneas en la división 1
    else:
        split1 = linessplit[
            n:
        ]  # Crea la primera división con el primer número "a" de líneas en la división 1
    return split1


def mapper(text):
    keyval = []
    for i in text:
        i = re.sub(r"[,\.\:]","",i)
        keyval.append([i, 1])  # Crea diccionario [palabra,1]
    return keyval


def sortedlists(list1, list2):
    out = list1 + list2  # Concatena listas
    out.sort(key=lambda x: x[0])  # Organiza palabras de orden alfabético
    return out


def reducer(part_out1):
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
    return sum_reduced


if __name__ == "__main__":

    texto = ""
    File = open("VC.pdf", "rb")
    data = PyPDF2.PdfReader(File)

    for i in range(0, len(data.pages)):
        page = data.pages[i]
        texto = texto + page.extract_text()

    cleanData = data_clean(texto)
    lineaSplits1 = splitlines(cleanData, int(len(cleanData) / 2), 1)
    lineaSplits2 = splitlines(cleanData, int(len(cleanData) / 2), 2)
    sortWords = sortedlists(mapper(lineaSplits1), mapper(lineaSplits2))

    re1 = reducer(sortWords)

    for i in range(0, len(re1)):
        print(re1[i])
