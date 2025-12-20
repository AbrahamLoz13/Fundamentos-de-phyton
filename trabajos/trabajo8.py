nombre_usuario = "aBrAhAm"
titulo_libro = "aprende PYTHON en 10 minutos"

# Misión 1: Queremos que el nombre quede solo con la primera mayúscula (Abraham)
nombre_correcto = nombre_usuario.capitalize() # <--- ¡Esto está mal!

# Misión 2: Queremos el título todo en minúsculas para buscarlo mejor
titulo_normalizado = titulo_libro.lower() # <--- ¡Esto también está mal!

print(f"Usuario: {nombre_correcto}")
print(f"Libro: {titulo_normalizado}")