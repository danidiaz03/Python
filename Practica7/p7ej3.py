personas=[("Dani",21),("Gemma",23),("Duende",4)]
nueva_lista=list(map(lambda p:(p[0],p[1]+1),personas))
print(nueva_lista)