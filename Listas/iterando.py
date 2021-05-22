def filtrar_pares(lista):
    respuesta=[]
    for i in range(0,len(lista)):
        if lista[i]%2==0:
            respuesta.append(lista[i])
    return respuesta

def filtrar_primos(lista):
    respuesta=[]
    for i in lista:
        if es_primo(i):
            respuesta.append(i)
    return respuesta
    
def es_primo(num):
    respuesta=True
    if num==1:
        respuesta=False
    else:
        for i in range(2,num):
            if num%i==0:
                respuesta=False
        
    return respuesta

def sumar_elementos(lista):
    suma=0
    for i in lista:
        suma+=i
    return suma

def esta_ordenada(lista):
    respuesta=0
    lista2=sorted(lista)
    if lista==lista2:
        respuesta=True
    else:
        respuesta=False
    return respuesta
            
def producto_escalar(vector_1, vector_2):
    respuesta=0
    for i in range(len(vector_1)):
        respuesta+= (vector_1[i]* vector_2[i])
    return respuesta

def letras_en_palabra(letras, frase):
    respuesta=0
    contador=0
    for i in range(len(letras)):
        if letras[i] in frase:
            contador+=1
    if contador==len(letras):
        respuesta=True
    else:
        respuesta= False
    return respuesta
        