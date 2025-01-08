personas={}

while True:
    nombre=input("Introduce Nombre / -1 para terminar\n")
    
    if nombre == "-1":
        break
    
    gusto=input("Introduce un gusto")
    
    if nombre not in personas:
        personas[nombre]=[gusto]
    else:
        if gusto not in personas[nombre]:
            personas[nombre].append(gusto)
            
print("\n Gustos de las personas")
for persona,gustos in personas.items():
    print(f"{persona}: {', '.join(gustos)}")       
    