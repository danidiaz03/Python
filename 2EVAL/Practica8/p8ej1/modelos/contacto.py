class Contacto():
    
    def __init__(self,nombre,telefono,email):
        self.__nombre=nombre
        self.__telefono=telefono
        self.__email=email
        

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre
    
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self,telefono):
        self.__telefono=telefono
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        self.__email=email

    def __str__(self):
        return f"Nombre: {self.__nombre}, Teléfono: {self.__telefono}, Email: {self.__email}"
