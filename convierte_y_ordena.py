def ordenar_lista(texto):
    '''Recibo un texto y lo convierte en una lista de palabras.
    Por ultimo ordena la lista.'''
    listanueva=texto.split()
    listanueva.sort()
    return listanueva