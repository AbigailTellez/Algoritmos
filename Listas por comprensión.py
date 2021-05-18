def numeros_positivos(numero):
    respuesta=[]
    for i in range(1,numero+1):
        respuesta.append(i)
    return respuesta

def numeros_positivos_pares(numero):
    respuesta=[]
    for i in range(2,numero+1):
        if i%2==0:
            respuesta.append(i)
    return respuesta

def numeros_positivos_pares_cuadrado(numero):
    respuesta=[]
    for i in range(2,numero+1):
        if i%2==0:
            respuesta.append(i**2)
    return respuesta

def impares_al_cuadrado(lista):
    respuesta=[]
    for i in lista:
        if i%2!=0:
            respuesta.append(i**2)
        else:
            respuesta.append(i)
    return respuesta

def filtrar_tuplas_por_suma(lista_de_tuplas):
    respuesta=[]
    for i in range(0,len(lista_de_tuplas)):
        if (lista_de_tuplas[i][0]+lista_de_tuplas[i][1])>=0:
            respuesta.append(lista_de_tuplas[i])
    return respuesta

def filtrar_tupla_elemento_par(lista_de_tuplas):
    respuesta=[]
    for i in range(0,len(lista_de_tuplas)):
        if lista_de_tuplas[i][0]%2==0 or lista_de_tuplas[i][1]%2==0:
            respuesta.append(lista_de_tuplas[i])
    return respuesta

def filtrar_tupla_elemento_par(lista_de_tuplas):
    respuesta=[]
    for i in range(0,len(lista_de_tuplas)):
        if lista_de_tuplas[i][0]%2==0 or lista_de_tuplas[i][1]%2==0:
            respuesta.append(lista_de_tuplas[i])
    return respuesta
