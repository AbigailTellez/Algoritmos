def sumar_caracteres_numericos(cadena):
    respuesta=0
    for x in cadena:
        if x.isnumeric():
            respuesta+=int(x)
    return respuesta