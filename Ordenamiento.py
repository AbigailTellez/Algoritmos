def ordenar_lista_menor_a_mayor(lista):
    return sorted(lista)

def ordenar_lista_mayor_a_menor(lista):
    listanueva=sorted(lista)
    return listanueva.reverse()

def ordenar_lista_alfabeticamente(lista):
    return sorted(lista)

def ordenar_palabras_por_longitud(lista):
    listanueva:[]
    for i in range (0,len(lista)):
        if len(lista[i])>len(listanueva[0]):
            listanueva.insert( 0, lista[i])
        else:
            if len