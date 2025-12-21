# Objetivo del problema:
# Normalizar cadenas de texto utilizando métodos integrados de Python para corregir 
# el formato de nombres propios y estandarizar títulos para búsquedas.

nombre_usuario = "aBrAhAm"
titulo_libro = "aprende PYTHON en 10 minutos"

# Resolución - Formateo de texto:

# #ejemplo de método capitalize()
# El objetivo es transformar un string para que solo la primera letra sea mayúscula
# y el resto minúsculas, sin importar cómo estaba escrito originalmente.
nombre_correcto = nombre_usuario.capitalize() 

# #ejemplo de método lower()
# El objetivo es convertir todos los caracteres del string a minúsculas.
# Es muy útil para bases de datos donde las búsquedas no deben distinguir entre A y a.
titulo_normalizado = titulo_libro.lower() 

# Impresión usando f-strings para mostrar los datos limpios
print(f"Usuario: {nombre_correcto}")
print(f"Libro: {titulo_normalizado}")