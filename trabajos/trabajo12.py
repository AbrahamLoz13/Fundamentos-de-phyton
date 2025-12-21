# Objetivo del problema:
# Analizar una cadena de texto para obtener su longitud, verificar su puntuación final, 
# localizar palabras específicas y transformar su formato a mayúsculas.

frase = input("escriba una frase: ")

# Resolución - Inspección de texto:

# #ejemplo de función len()
# El objetivo es contar el número total de caracteres (incluyendo espacios) en el string.
caracteres_frase = len(frase)
print(f"La cantidad de carácteres de la frase es {caracteres_frase}")

# #ejemplo de método endswith()
# El objetivo es validar si la frase termina con un carácter específico, en este caso un punto.
# Devuelve un valor booleano (True/False).
termina_frase = frase.endswith(".")
print(termina_frase)

# #ejemplo de método find()
# El objetivo es buscar la posición del índice donde comienza la palabra "Python".
# Recuerda que devuelve -1 si no la encuentra.
encuentra_frase = frase.find("Python")
print(encuentra_frase)

# #ejemplo de método upper()
# El objetivo es convertir toda la cadena a letras mayúsculas.
frase_mayusculas = frase.upper()
print(frase_mayusculas)