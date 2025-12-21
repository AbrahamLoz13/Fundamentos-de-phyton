# Objetivo del problema:
# Implementar una lógica de decisión basada en colores de un semáforo utilizando
# la estructura condicional if-elif-else para ejecutar diferentes acciones.

color = "verde"

# Resolución - Control de flujo:

# #ejemplo de sentencia if
# El objetivo es evaluar la condición primaria. Si es verdadera, se ejecuta este bloque.
if color == "verde":
    print("puedes pasar")

# #ejemplo de sentencia elif (else if)
# El objetivo es evaluar una segunda condición específica solo si la primera fue falsa.
elif color == "amarillo":
    print("avanza con precaución")

# #ejemplo de sentencia else
# El objetivo es definir una acción por defecto si ninguna de las condiciones anteriores se cumplió.
else:
    print("no puedes avanzar")