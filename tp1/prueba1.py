def main():
    aciertos=0
    desaciertos=0
    palabras_encontradas=0
    palabrasmalas=[]
    palabra='aceituna'                                                              #Falta funcion que me elija una palabra al azar
    adivinar= lista_de_palabra(palabra)                                           
    adivino="0"
    while palabras_encontradas!=len(palabra) and desaciertos<=7:
        imprime_juego(adivino,adivinar,aciertos,desaciertos,palabrasmalas)         #imprime como va el juego
        letra=pedir_letra()                                                        #pide y devuelve una letra
                                                                                   #falta funcion para validar la letra
        if letra in palabra:
            aciertos+=1
            adivino=True
            for i in range(0, len(palabra)):
                if palabra[i]==letra:
                    palabras_encontradas+=1
                    adivinar[i]=letra   
        else:
             desaciertos+=1
             adivino=False
             palabrasmalas.append(letra)
             
    gano_o_perdio(palabras_encontradas,palabra)      
   
def lista_de_palabra(palabra):
    '''recibe una palabra y devuelve una lista con los signos de pregunta(?)'''
    lista=[]
    for i in palabra:
        lista+='?'
    return lista
    
def imprime_juego(adivino,adivinar,aciertos,desaciertos,palabrasmalas):
    '''imprime todo el juego'''
    if adivino==False:
        print('Lo siento!!! ', ' '.join(adivinar), 'Aciertos: ', aciertos, 'Desaciertos: ', desaciertos, '-', ' '.join(palabrasmalas))    
    elif adivino==True:
        print('Muy bien!!! ', ' '.join(adivinar), 'Aciertos: ', aciertos, 'Desaciertos: ', desaciertos, '-', ' '.join(palabrasmalas))
    else:
        print('Palabra a adivinar: ', ' '.join(adivinar), 'Aciertos: ', aciertos, 'Desaciertos: ', desaciertos, '-', ' '.join(palabrasmalas))
        
             
def pedir_letra():
    '''pide y devuelve una letra'''
    letra=input('Ingrese una letra: ')     
    return letra


def gano_o_perdio(palabras_encontradas,palabra):
    '''imprime si gano o perdio el jugador'''
    if palabras_encontradas==len(palabra):
        print('FELICIDADES GANASTE')
    else:
        print('Lo siento, PERDISTE')
main()

    
