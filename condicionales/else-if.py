
#el elif sirve como otra opción en caso de que la primera no se cumpla

#se puede poner un if dentro de un if
ingreso_mensual = 11000
gasto_mensual = 600
if ingreso_mensual >= 10000:
    if gasto_mensual <= 7000:
        print("estás gastando bien")
    else:
        print("estás gastando mucho")
    
elif ingreso_mensual >= 1000:
    print("estás bien en cualquier parte de LATAM")

elif ingreso_mensual >= 500:
    print("estás bien ecnómicamente en argentina")
    
else:
    print("eres pobre")
