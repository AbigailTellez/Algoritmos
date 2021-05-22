def precendencia_de_caracteres(cadena, caracter_1, caracter_2):
    respuesta=0
    for i in range(0,len(cadena)):
        if cadena[i]==caracter_1 and cadena[i+1]==caracter_2:
            respuesta+=1
    return respuesta
            