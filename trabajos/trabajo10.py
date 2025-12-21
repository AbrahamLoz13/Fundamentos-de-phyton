# Objetivo del problema:
# Detectar palabras prohibidas dentro de un texto ingresado por el usuario,
# normalizando el contenido para evitar evasiones por mayúsculas y validando
# la posición del término mediante el método find().

prohibidas = ["tonto", "feo", "puto"] 
mensaje = input("Escriba lo que usted quiera: ")

# Resolución - Procesamiento de texto:

# #ejemplo de normalización
# El objetivo es asegurar que la búsqueda sea efectiva sin importar si el usuario
# escribe en mayúsculas o minúsculas.
mensaje_normalizado = mensaje.lower()

# #ejemplo de método find()
# El objetivo es buscar la subcadena "tonto". 
# Si find() devuelve algo distinto de -1, significa que la palabra fue encontrada.
if mensaje_normalizado.find("tonto") != -1:
    print(" MENSAJE BLOQUEADO, LLAMANDO A LA POLICÍA...") 
else:
    # Si devuelve -1, la palabra no existe en el mensaje.
    print(f" Mensaje enviado: {mensaje}")