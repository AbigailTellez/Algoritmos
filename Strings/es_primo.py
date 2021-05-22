def es_primo(num):
    respuesta=True
    if num==1:
        respuesta=False
    else:
        for i in range(2,num):
            if num%i==0:
                respuesta=False
        
    return respuesta