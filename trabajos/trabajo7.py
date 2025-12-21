# Objetivo del problema:
# Determinar la elegibilidad de una beca basándose en criterios académicos y geográficos
# utilizando operadores lógicos combinados (or, and) y agrupamiento con paréntesis.

# #ejemplo de conversión de tipos (casting)
# El objetivo es convertir la entrada de texto (input) a número decimal (float).
promedio = float(input("cual es tu promedio? "))
distancia = float(input("cual es tu distancia en kilómetros? "))
es_estudiante = True

# Resolución - Evaluación de criterios combinados:

# #ejemplo de jerarquía de operadores
# El objetivo es que se cumpla al menos una de las condiciones dentro del paréntesis:
# (Promedio alto O Gran distancia) Y además que obligatoriamente sea estudiante.
if (promedio >= 9 or distancia > 40) and es_estudiante == True:
    print("beca concedida")
else:
    # Si no es estudiante o no cumple ninguno de los criterios numéricos, se deniega.
    print("beca denegada")