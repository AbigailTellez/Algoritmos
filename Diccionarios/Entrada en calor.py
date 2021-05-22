def numeros_al_cuadrado(numero):
    respuesta = {}
    for i in range(1,numero+1):
        respuesta[i]=i**2
    return respuesta
    
def mezclar_diccionarios(dicc_uno, dicc_dos):
    diccionario={}
    for clave in dicc_uno:
        diccionario[clave]=dicc_uno[clave]
    for clave in dicc_dos:
        diccionario[clave]=dicc_dos[clave]
    return diccionario

def filtrar_por_sumar_diez(diccionario):
    respuesta={}
    for clave in diccionario:
        if clave + diccionario[clave]>=10:
            respuesta[clave]= diccionario[clave]
    return respuesta

def ordenar_valores_por_longitud(diccionario):
    respuesta=[]
    for clave in diccionario:
        respuesta.append(diccionario[clave])
    return sorted(respuesta, key=None, reverse=False)