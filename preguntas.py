"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

x = open("data.csv", "r").readlines()
x = [z.replace("\n", "") for z in x]
x = [z.split("\t") for z in x]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    y = [z[1] for z in x[0:]]
    Columna_2 = []
    for i in y:
        j = int(i)
        Columna_2.append(j)
    return sum(Columna_2)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    from collections import Counter
    from operator import itemgetter

    y = [z[0] for z in x[0:]]

    m = (list(Counter(y).most_common()))

    m.sort(key=itemgetter(0), reverse=False)

    return m


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    y = [z[0:2] for z in x[0:]]

    Tuplas = list(map(tuple, y))

    sorted_tupla = sorted(Tuplas, key=lambda x: x[0])

    nueva_tupla = [(x[0], int(x[1])) for x in sorted_tupla]

    diccionario={}
    for key, value in nueva_tupla:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
        
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, sum(value))
        new_sequence.append(tupla)

    return new_sequence


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    y = [z[2].split("-")[1] for z in x[0:]]

    new_fecha = []
    for word in y:
        new_fecha.append((word, 1))

    sorted_fecha = sorted(new_fecha, key=lambda x: x[0])

    diccionario={}
    for key, value in sorted_fecha:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
        
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, sum(value))
        new_sequence.append(tupla)

    return new_sequence



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    y = [z[0:2] for z in x[0:]]
    Tuplas = list(map(tuple, y))
    sorted_tupla = sorted(Tuplas, key=lambda x: x[0])
    nueva_tupla = [(x[0], int(x[1])) for x in sorted_tupla]

    diccionario={}
    for key, value in nueva_tupla:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
        
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, max(value), min(value))
        new_sequence.append(tupla)

    return new_sequence


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    y = [z[4].split(",") for z in x[0:]]
    Tuplas = list(map(tuple, y))

    tuplas_individuales = []

    for tupla in Tuplas:
        elementos_tupla = []

        for elemento in tupla:
            clave, valor = elemento.split(':')
            elementos_tupla.append((clave, int(valor)))  
        tuplas_individuales.append(tuple(elementos_tupla))

    lista_combinada = [tupla for tuplas_internas in tuplas_individuales for tupla in tuplas_internas]
    sorted_tupla = sorted(lista_combinada, key=lambda x: x[0])

    diccionario={}
    for key, value in sorted_tupla:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
        
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, min(value), max(value))
        new_sequence.append(tupla)

    return new_sequence


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    y = [z[0:2] for z in x[0:]]
    Tuplas = list(map(tuple, y))
    sorted_tupla = sorted(Tuplas, key=lambda x: x[1])
    Tuplass = [tuple(reversed(tupla)) for tupla in sorted_tupla]

    diccionario={}
    for key, value in Tuplass:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
        
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(int(key), value)
        new_sequence.append(tupla)   

    return new_sequence


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    y = [z[0:2] for z in x[0:]]
    Tuplas = list(map(tuple, y))
    sorted_tupla = sorted(Tuplas, key=lambda x: x[1])
    Tuplass = [tuple(reversed(tupla)) for tupla in sorted_tupla]

    diccionario={}
    for key, value in Tuplass:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
        
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, value)
        new_sequence.append(tupla)

    nueva_lista = [(x[0], sorted(list(set((x[1]))))) for x in new_sequence]

    return nueva_lista
    

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    y = [z[4].split(",") for z in x[0:]]
    Tuplas = list(map(tuple, y))

    tuplas_individuales = []

    for tupla in Tuplas:
        elementos_tupla = []

        for elemento in tupla:
            clave, valor = elemento.split(':')
            elementos_tupla.append((clave, 1))  
        tuplas_individuales.append(tuple(elementos_tupla))

    lista_combinada = [tupla for tuplas_internas in tuplas_individuales for tupla in tuplas_internas]
    sorted_tupla = sorted(lista_combinada, key=lambda x: x[0])

    diccionario={}
    for key, value in sorted_tupla:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
        
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, sum(value))
        new_sequence.append(tupla)

    return dict(new_sequence)


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    y = [[z[0], z[3], z[4]] for z in x[0:]]
    Tuplas = list(map(tuple, y))
    nueva_lista = [(x[0], len((x[1].split(','))), len(x[2].split(','))) for x in Tuplas]

    return nueva_lista


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    y = [[z[1], z[3]] for z in x[0:]]
    Tuplas = list(map(tuple, y))
    new_tuplas = [(int(x[0]), (x[1].split(','))) for x in Tuplas]

    tuplas_separadas = []
    for tupla in new_tuplas:
        valor1 = tupla[0]
        lista = tupla[1]
        nuevas_tuplas = [(valor1, elemento) for elemento in lista]
        tuplas_separadas.extend(nuevas_tuplas)
        
    sorted_tupla = sorted(tuplas_separadas, key=lambda x: x[1])
    Tuplass = [tuple(reversed(tupla)) for tupla in sorted_tupla]


    diccionario={}
    for key, value in Tuplass:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
        
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, sum(value))
        new_sequence.append(tupla)

    return dict(new_sequence)


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    y = [[z[0], z[4].split(",")] for z in x[0:]]
    Tuplas = list(map(tuple, y))
    new = [(x[0], (tuple(x[1]))) for x in Tuplas]

    diccionario={}
    for key, value in new:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
        
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, value)
        new_sequence.append(tupla)

    lista_tuplas = []

    for letra, tuplas in new_sequence:

        temp_list = []
        for tup in tuplas:
            temp_list.extend(tup)
        lista_tuplas.append((letra, (tuple(temp_list))))

    tuplas_separadas = []
    for tupla in lista_tuplas:
        letra = tupla[0]
        lista = tupla[1]
        nuevas_tuplas = [(letra, elemento) for elemento in lista]
        tuplas_separadas.extend(nuevas_tuplas)

    nuevas_tuplas = [(t[0], int(t[1].split(":")[1])) for t in tuplas_separadas]

    diccionario={}
    for key, value in nuevas_tuplas:
        if key not in diccionario.keys():
            diccionario[key]=[]
        diccionario[key].append(value)
        
    new_sequence=[]
    for key, value in diccionario.items():
        tupla=(key, sum(value))
        new_sequence.append(tupla)

    sorted_tupla = sorted(new_sequence, key=lambda x: x[0])    

    return dict(sorted_tupla)
