facturas={
    
}

cant_pagada=0
cant_pendiente=0

while True:
    
    print(f"Cantidad pagada hasta el momento: {cant_pagada}")
    
    opcion=input('Introduce opcion\n1:Ver facturas pendientes de pago\n2:Añadir nueva factura\n3:Salir\n')
    
    if opcion=='1':
        print(facturas)
        opcion2=input("Introduce opcion: \n1:Pagar factura\n2:Salir\n")

        if opcion2 == '1':
            num_factura=input("introduce el numero de factura\n")
            if num_factura in facturas.keys():
                cant_pagada+=facturas[num_factura]
                cant_pendiente-=facturas[num_factura]
                del facturas[num_factura]
        elif opcion2=='2':
            continue
        else:
            print("Opción no válida")
    
    elif opcion=='2':
        num_factura=input("Introduce número de factura\n")
        if num_factura not in facturas.keys():
            coste=input("Introduce coste:\n")
            facturas[num_factura]=coste
            cant_pendiente+=coste
        else:
            print("Numero de factura ya existente")
    
    elif opcion=='3':
        break
    
    else:
        print("OPcion no válida")