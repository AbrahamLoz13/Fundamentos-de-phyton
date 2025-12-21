# Objetivo del problema:
# Validar el acceso a un sistema comparando entradas del usuario con datos predefinidos
# utilizando la función input() y el operador lógico 'and' para verificar múltiples condiciones.

user_real = "admin"
pass_real = "1234"

# #ejemplo de entrada de datos
# El objetivo es capturar la información que el usuario escribe en la consola.
user_escrito = input("Esribe tu user: ")
pass_escrito = input("Escribe tu contraseña: ")

# Resolución - Validación simultánea:

# #ejemplo de operador lógico 'and'
# El objetivo es que ambas comparaciones sean True para permitir el acceso.
# Si el usuario o la contraseña fallan, la expresión completa resulta en False.
if user_escrito == user_real and pass_real == pass_escrito:
    print("accediendo correctamente")
else:
    # El objetivo es manejar cualquier caso donde los datos no coincidan.
    print("Datos incorrectos")