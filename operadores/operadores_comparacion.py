# APUNTES: Operadores de comparacion
# Estos operadores devuelven un valor booleano: True (Verdadero) o False (Falso)

# ejemplo de igualdad
es_igual = 5 == 6
print(es_igual) # False

# ejemplo de diferencia (distinto de)
es_diferente = 5 != 6
print(es_diferente) # True

# ejemplo de mayor que
mayor_que = 5 > 6
print(mayor_que) # False

# ejemplo de menor que
menor_que = 5 < 6
print(menor_que) # True

# ejemplo de mayor o igual que
mayor_o_igual = 5 >= 6
print(mayor_o_igual) # False

# ejemplo de menor o igual que
menor_o_igual = 5 <= 6
print(menor_o_igual) # True


# ejemplo de comparacion combinada con aritmetica
# Python resuelve primero la suma (5 + 10) y luego compara el resultado
a = 5
b = 10
c = 15
comparacion = a + b < c

print(comparacion) # False (porque 15 no es menor que 15)


# ejemplo de comparacion de cadenas (texto)
contraseña_almacenada = "Abraham1"
contraseña_escrita = "Abraham1"

print(contraseña_almacenada == contraseña_escrita) # True