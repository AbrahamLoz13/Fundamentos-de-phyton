# Objetivo del problema:
# Validar un nombre de usuario de forma insensible a mayúsculas/minúsculas, 
# asegurando que la comparación sea técnica y la respuesta visualmente correcta.

# #ejemplo de captura de datos
nombre_usuario = input("Ingrese su nombre: ")

# Resolución - Estandarización para comparación:

# #ejemplo de método lower()
# El objetivo es transformar la entrada para que coincida con la base de datos (admin).
# No importa si escribió ADMIN, Admin o adMiN, se volverá "admin".
nombre_usuario_min = nombre_usuario.lower()

# #ejemplo de condicional de igualdad
if nombre_usuario_min == "admin":
    # #ejemplo de método capitalize()
    # El objetivo es mostrar el nombre con formato de nombre propio (Abraham) 
    # únicamente al momento de imprimir el mensaje de éxito.
    print(f"Acceso concedido, bienvenido {nombre_usuario.capitalize()}")
else:
    # El objetivo es manejar accesos no autorizados.
    print("Acceso denegado")