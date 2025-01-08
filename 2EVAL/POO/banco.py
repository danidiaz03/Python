from tarjeta import Tarjeta
from tarjetajoven import TJoven

t=Tarjeta("1111A")
q=Tarjeta("2222B",2000)

print(t.consultar_saldo())

print(Tarjeta.comision) #Se puede poner porque es una variable estática

#print(Tarjeta.saldo)  Salta error porque es atributo del objeto

print(t._Tarjeta__saldo)

print(t.saldo)

t.saldo=3000

print(t.saldo)

t.ingresar(500)

print(t.saldo)

t.reintegrar(100)

print(t.saldo)

print(t)

t+q

print(t)
print(q)

r=TJoven("444D",20,300)

r.bono_cumple()

print(r)