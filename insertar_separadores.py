def insertar_separadores(cadena, separador, espaciado):
    respuesta=""
    contador=0
    for x in cadena:
        if contador%espaciado==0 and contador!=0:
            respuesta+=separador
        respuesta+=x
        contador+=1
    return respuesta