def eliminar_repetidas(texto):
    '''Recibe un texto y me arme una lista. Lo que me devuelve es una
    lista sin palabras repetidas y ordenadas'''
    listanueva=texto.split()
    listanueva.sort()
    for i in listanueva:
        if listanueva.count(i)>=2:
            listanueva.remove(i)
    return listanueva

eliminar_repetidas("hola mama hola")
eliminar_repetidas("si te dije que si")