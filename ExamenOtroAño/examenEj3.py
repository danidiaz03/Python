l=[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]




def anyadir_precio(d):
    d['precio']=d['metros']*100+d['habitaciones']*5000+d['garaje']*15000 * d['año']/100
    if d['zona']=='B':
        d['precio']=d['precio']*1.5
    
    
for d in l:
    anyadir_precio(d)
print(l)

p= int(input("Precio: "))


l_busqueda=list(filter(lambda x: x['precio']<p,l))
print(l_busqueda)
