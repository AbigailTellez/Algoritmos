def ultimos_tres_elementos(lista): 
    listanueva=lista[-3:]
    return listanueva

def ultimos_tres_elementos_concatenados(lista):
    respuesta=[]
    for i in range(0,len(lista)):
        respuesta+=lista[i]
    return respuesta

def indices_pares(lista):
    respuesta=[]
    for i in range(0,len(lista)):
        if i%2==0:
            respuesta.append(lista[i])
    return respuesta

def indices_impares(lista):
    respuesta=[]
    for i in range(0,len(lista)):
        if i%2!=0:
            respuesta.append(lista[i])
    return respuesta

def invertir(lista):
    respuesta=[]
    for i in range(1,len(lista)+1):
        respuesta.append(lista[-i])
    return respuesta
