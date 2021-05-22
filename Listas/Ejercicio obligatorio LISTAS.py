def es_primo(num):
    respuesta=True
    if num==1:
        respuesta=False
    else:
        for i in range(2,num):
            if num%i==0:
                respuesta=False
        
    return respuesta

def filtrar_primos(numeros, menor_numero):
    resultado=[]
    for i in numeros:
        if es_primo(i) and i>menor_numero:
            resultado.append(i)
    return resultado

def ordenar_por_longitud_de_tuplas(tuplas):
    resultado=[]
    tuplas.sort(key = lambda x: len(x))
    for i in range(1,len(tuplas)+1):
        resultado.append(tuplas[-i])
    return resultado

def concatenar_primeros_elementos(lista):
    resultado=[]
    for i in range(0,len(lista)):
        resultado.append(lista[i][0])
        resultado.append(lista[i][1])
    return resultado