def filtrador_de_vocales(cadena):
    '''Completar el cuerpo de la función. La misma recibe una
cadena y debe retornar la misma habiendo filtrado todas las
vocales que contenía.'''
    nuevacadena=""
    vocales='aeiou'
    for i in cadena:
        if i not in vocales:
            nuevacadena+=i
    return nuevacadena