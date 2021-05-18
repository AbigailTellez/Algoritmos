def ordenar_lista_menor_a_mayor(lista):
    return sorted(lista)

def ordenar_lista_mayor_a_menor(lista):
    return lista.sort(key= None, reverse=True)

def ordenar_lista_alfabeticamente(lista):
    return sorted(lista)

def ordenar_palabras_por_longitud(lista):
    return lista.sort(key= lambda x:len(x), reverse=True)

def ordenar_lista_por_tupla(lista):
    return lista.sort(key= lambda x: x[1], reverse=True)

def ordenar_lista_por_suma_tupla(lista):
    return lista.sort(key=lambda x: x[0]+x[1], reverse=True)