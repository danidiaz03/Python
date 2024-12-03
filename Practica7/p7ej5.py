alumnos={"Ana":8,"DAni":5,"Pedro":3,"Pablo":1}

aprobados={k:v for k,v in alumnos.items() if v>=5}
print(aprobados)

suspensos={k:v for k,v in alumnos.items() if v<5}
print(suspensos)

nota=7
nota_superior={k:v for k,v in alumnos.items() if v>=nota}
print(nota_superior)