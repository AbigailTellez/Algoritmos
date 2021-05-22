def pedir_partidos():
    return input("Ingrese el partido a sumarle votos: ")

def pedir_votos():
    return int(input('Ingrese la cantidad de votos a sumarle: '))

def preguntar_si_sigue():
    continua=input("Desea seguir ingresando?(s/n): ")
    respuesta=0
    if continua=="s":
        respuesta=True
    elif continua== "n":
        respuesta=False
    return respuesta
         
def mostrar_resultado(diccionario):
    lista=list(diccionario.items())
    lista.sort(key= lambda x: x[1], reverse=True)
    for i in range (0,len(lista)):
        print('El partido ', lista[i][0], 'obtuvo ', lista[i][1], 'votos') 
        

def votaciones():
    sigue=True
    diccionario={}
    while sigue==True:
        partido=pedir_partidos()
        votos=pedir_votos()                  
        if partido in diccionario:
            diccionario[partido]+=votos
        else:
            diccionario[partido]=votos
        sigue=preguntar_si_sigue()           #devuelve True o False
    
    mostrar_resultado(diccionario)
    
    
votaciones()