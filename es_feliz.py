def es_feliz():
    comentario=input('ingrese el comentario ')
    nombre=input('ingrese nombre ')
    puntos=0
    masfeliz=[]
    while comentario!='salir' or nombre!='salir':
        puntos2=puntos_feli(comentario,nombre)
        if puntos < puntos2:
            masfeliz.clear()
            masfeliz.append(nombre)
            puntos=puntos2
        comentario=input('ingrese el comentario ')
        nombre=input('ingrese nombre ')
        
    print('Es mas feliz', masfeliz[0])
    

def puntos_feli(comentario,nombre):
    puntosfeli=0
    lista=comentario.split()
    for i in range(0,len(lista)):
        if "feliz" in lista[i] or "felic" in lista[i]:
            puntosfeli+=1
    return puntosfeli

es_feliz()     