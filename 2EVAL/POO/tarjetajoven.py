from tarjeta import Tarjeta

class TJoven(Tarjeta):
    def __init__(self,identificador,edad,cantidad=200):
        super().__init__(identificador,cantidad)
        self.__edad=edad
        
        
    @property
    def edad(self):
       return self.__edad
        
    @edad.setter
    def edad(self,edad):
        self.__edad=edad
            
    def __str__(self):
        return super().__str__() + "\n" + "Edad: " + str(self.__edad)
        
    def reintegrar(self,cantidad):
         self.__saldo-=cantidad
            
    def bono_cumple(self):
            if self.__edad<=22:
                self.saldo+=20
        