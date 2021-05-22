def palabra_mas_larga(texto):
    """ recibe un texto y debe retornar cuál es la palabra más larga
del mismo. Se puede asumir que todas las palabras están separadas por
espacios y no hay caracteres especiales."""
    lista=texto.split()
    palabragrande=""
    for i in range(0,len(lista)):
        if len(lista[i]) > len(palabragrande):
            palabragrande=lista[i]
            
    return palabragrande


palabra_mas_larga("Hola como estas este es un texto de prueba")
palabra_mas_larga("Quiero aprobar algoritmos y algebra") 