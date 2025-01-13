from modelos.agenda import Agenda
agenda = Agenda()
while True:
    opc=int(input("Selecciona opcion:\n1.Añadir Contacto\n2.Buscar contacto\n3.Listar contactos\n4.Eliminar contactos\n"))
    if opc == 1:
        nombre=input("\nIntroduce nombre\n")
        telefono=input("\nIntroduce telefono\n")
        email=input("\nIntroduce email\n")
        agenda.añadirContacto(nombre,telefono,email)
    if opc == 3:
        agenda.mostrarContactos()