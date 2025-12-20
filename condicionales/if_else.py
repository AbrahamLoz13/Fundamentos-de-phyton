# APUNTES: Estructura If-Else y Flujo de Ejecucion

# ejemplo de condicion simple (mayor o igual que)
edad = 17

if edad >= 18:
    print("Puedes pasar")
else:
    print("No puedes pasar")

# Esta linea se ejecuta siempre porque esta fuera de la identacion del if
print("Este texto no forma parte de ninguna condicion")


# ejemplo de comparacion de igualdad (==)
contraseña_almacenada = "1234"
contraseña_escrita = "1234"

if contraseña_almacenada == contraseña_escrita:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")