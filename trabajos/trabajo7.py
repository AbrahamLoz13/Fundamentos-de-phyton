promedio = float(input("cual es tu promedio? "))
distancia = float(input("cual es tu distancia en kilómetros? "))
es_estudiante = True

if (promedio >= 9 or distancia > 40) and es_estudiante == True:
    print("beca concedida")
else:
    print("beca denegada") 
    