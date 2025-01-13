from .contacto import Contacto

class Agenda():
# Lista de contactos
    __usuarios = []
    

    def añadirContacto(self,nombre,telefono,email):
        c=Contacto(nombre,telefono,email)
        self.__usuarios.append(c)
        print("Contacto añadido")
        

    def mostrarContactos(self):
        for contacto in self.__usuarios:
            print(contacto)