from .contacto import Contacto

class Agenda():
# Lista de contactos
    __usuarios = []
    

    def añadirContacto(self,nombre,telefono,email):
        c=Contacto(nombre,telefono,email)
        self.__usuarios.append(c)
        print("Contacto añadido")
    
    
    def buscarContacto(self,criterio,dato):
        if criterio == 'nombre':
            for i in self.__usuarios:
                if i.nombre == dato:
                    return True
            return False
        if criterio == 'email':
            for i in self.__usuarios:
                if i.email == dato:
                    return True
            return False
        if criterio == 'telefono':
            for i in self.__usuarios:
                if i.telefono == dato:
                    return True
            return False
        
    def eliminarContacto(self, dato, criterio='nombre'):
        # Elimina el contacto basándose en el criterio elegido ('nombre', 'email' o 'telefono')
        if criterio == 'nombre':
            self.__usuarios = list(filter(lambda c: c.nombre != dato, self.__usuarios))
        elif criterio == 'email':
            self.__usuarios = list(filter(lambda c: c.email != dato, self.__usuarios))
        elif criterio == 'telefono':
            self.__usuarios = list(filter(lambda c: c.telefono != dato, self.__usuarios))
        print("Contacto eliminado")

    def mostrarContactos(self):
        for contacto in self.__usuarios:
            print(contacto)
            
    
    