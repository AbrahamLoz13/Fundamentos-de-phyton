# Misión: Corregir este código

usuario = ("Abraham", 22, "12345") # Esto es una Tupla con (Nombre, Edad, Contraseña)

# Error 1: Intentamos cambiar el nombre en una Tupla (no se puede en una tupla)
# usuario[0] = "Jafet" 

# Error 2: Concatenación incorrecta de número con texto sin f-string o conversión (faltaba {})
mensaje = f"La edad del usuario es {usuario[1]}"

# Error 3: Diccionario mal definido (falta algo visual) (faltaba las ,)
datos_extra = {
    "Ciudad": "Aguascalientes",
    "Pais": "Mexico"
}

print(mensaje)
print(datos_extra["Pais"])