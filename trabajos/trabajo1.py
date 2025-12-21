# Definición de una tupla (Nombre, Edad, Contraseña)
# #ejemplo de estructura inmutable
usuario = ("Abraham", 22, "12345") 

# Resolución Error 1: 
# El objetivo era modificar un dato, pero las tuplas no lo permiten.
# Se mantiene como comentario porque causaría un TypeError.
# usuario[0] = "Jafet" 

# Resolución Error 2: 
# #ejemplo de formateo de texto
# El objetivo es integrar un entero dentro de una cadena. 
# Se utiliza f-string para permitir la interpolación de {usuario[1]}.
mensaje = f"La edad del usuario es {usuario[1]}"

# Resolución Error 3: 
# #ejemplo de definición de diccionario
# El objetivo es crear un mapa de clave:valor.
# Se corrigió agregando la coma necesaria para separar los elementos del diccionario.
datos_extra = {
    "Ciudad": "Aguascalientes",
    "Pais": "Mexico"
}

# Impresión de resultados
print(mensaje)
print(datos_extra["Pais"])