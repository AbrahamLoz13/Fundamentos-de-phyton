# Objetivo del problema:
# Asegurar la integridad del programa validando que la entrada del usuario sea un número 
# antes de realizar conversiones de tipo y comparaciones lógicas.

edad_texto = input("Dime tu edad: ")

# Resolución - Validación de caracteres:

# #ejemplo de método isnumeric()
# El objetivo es verificar si el string contiene únicamente caracteres numéricos.
# Esto evita que el programa colapse (crash) al intentar convertir letras a entero.
if edad_texto.isnumeric():
    
    # #ejemplo de conversión de tipo (int)
    # Una vez validado, se convierte el texto a número para poder comparar rangos.
    edad_in = int(edad_texto)
    
    # El objetivo es clasificar al usuario según su valor numérico.
    if edad_in >= 18:
        print("eres mayor de edad")
    else:
        print("eres menor de edad")
        
else:
    # El objetivo es manejar el error de entrada de forma amigable.
    print("por favor escriba numeros solamente")