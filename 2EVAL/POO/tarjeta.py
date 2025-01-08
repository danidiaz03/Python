class Tarjeta():
    comision=0.5
    
    def __init__(self,id,cantidad=1000):
        self.__id=id
        self.__saldo=cantidad
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,cantidad):
        self.__saldo=cantidad

    @property
    def identificador(self):
        return self.__id
    
    @identificador.setter
    def identificador(self,ident):
        self.__id=ident
    
    def __str__(self):
        return "id " + str(self.__id) + "\n" + "Saldo: " + str(self.__saldo)
    
    def __add__(self,otraTarjeta):
        self.__saldo+=otraTarjeta.__saldo
        otraTarjeta.__saldo=0
    
    
        
    def consultar_saldo(self):
        return self.__saldo
    
    def ingresar(self,cantidad):
        self.__saldo+=cantidad
    def reintegrar(self,cantidad):
        if(cantidad+cantidad*self.comision>self.__saldo):
            return False
        self.__saldo-=cantidad+cantidad*self.comision 