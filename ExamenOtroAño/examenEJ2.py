cadena = """nif;nombre;email;teléfono;descuento\n01234567X;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""


lines = cadena.split('\n')
claves = lines[0].split(';')
clientes_dict = {}

for line in lines[1:]:
    valores = line.split(';')
    cliente_dict={}
    for c,v in zip(claves[1:],valores[1:]):
        cliente_dict[c]=v
  
    clientes_dict[valores[0]] = cliente_dict

print()
print()
for item in clientes_dict.items():
    print("--------------------------------------")
    print("Cliente - " + item[0])
    print(item[1])
   