def funcion3(sitios_empleados,sitios_trabajo):
    personas = {}
    with open(sitios_empleados, "r") as f:
        for linea in f:
            datos= linea.strip().split("|")
            if datos[0] not in personas:
                if(datos[1] not in sitios_trabajo):
                    personas[datos[0]]=[[datos[1],datos[2]]]
            else:
                if datos[1] not in sitios_trabajo:
                    personas[datos[0]].append([datos[1],datos[2]])
                        
    for c,v in zip(personas.keys(),personas.values()):
       print(str(c)+" : " +str(v))
    return personas

