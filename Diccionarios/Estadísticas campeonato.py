campeonato = {
    "Boca": (2, 3, 4, 10, 10),
    "River": (3, 4, 2, 12, 16),
    "Central": (7, 1, 1, 23, 21),
    "Racing": (5, 2, 2, 15, 8),
    "Independiente": (4, 3, 2, 7, 8),
    "San Lorenzo": (1, 8, 0, 5, 9),
    "Godoy Cruz": (3, 3, 1, 3, 3),
    "Estudiantes": (1, 1, 7, 9, 9),
    "Huracan": (3, 2, 4, 4, 6),
    "Gimnasia LP": (0, 2, 7, 1, 26)
}
def main():
    ganador_y_perdedor(campeonato)
    empato(campeonato)
    proporcion(campeonato)
    
def ganador_y_perdedor(campeonato):
    dic={}
    for clave in campeonato:
        dic[clave]=campeonato[clave][0]*3
        dic[clave]+=campeonato[clave][1]
    lista=list(dic.items())
    lista.sort(key= lambda x: x[1], reverse=True)
    print("El equipo campeon es" ,lista[0][0], "con", lista[0][1], "puntos.")
    print("El equipo que desciende es" ,lista[-1][0], "con", lista[-1][1], "puntos.")

def empato(campeonato):
    dic={}
    for clave in campeonato:
        dic[clave]= campeonato[clave][1]
    lista= list(dic.items())
    lista.sort(key= lambda x: x[1], reverse=True)
    print('El equipo que mas partidos empato es', lista[0][0], 'con', lista[0][1],'partidos.')

def proporcion(campeonato):
    dic={}
    for clave in campeonato:
        dic[clave]=campeonato[clave][3]/campeonato[clave][4]
    lista=list(dic.items())
    lista.sort(key= lambda x: x[1], reverse=True)
    print("El equipo con mejor proporcion goleadora es {} con {}. ".format(lista[0][0],lista[0][1]))

main()