EDAD=2
empleados= [
            ['Juan','Obrero',37],
            ['Maria','ingeniera',55],
            ['Ignacio', 'Ingeniero', 60],
            ['ines','rrhh','23'],
            ]

empleados_antiguos= list(filter(lambda empleado:\empleado[EDAD]> 50 , empleados))
                         
print("[")
for empleado in empleados_antiguos:
    nombre, empleo, edad=empleado
    print(f"\t[{nombre},{empleo},{edad}]")
print("]")
                         