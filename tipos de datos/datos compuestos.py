# APUNTES: Listas, Tuplas, Conjuntos y Diccionarios

# LISTAS
# Van entre corchetes [] y su contenido se puede modificar
# ejemplo de lista simple con diferentes tipos de datos
lista = ["Leonardo", "12346", 9, True]
print(lista)

# ejemplo de modificacion y acceso por indices (empiezan en 0)
lista_datos = ["Maria", "Mujer", 10, False]

# Modificamos el primer elemento (posicion 0)
lista_datos[0] = "Ana"

print(lista_datos[0]) # Imprimira Ana
print(lista_datos[1]) # Imprimira Mujer
print(lista_datos[2]) # Imprimira 10
print(lista_datos[3]) # Imprimira False


# TUPLAS
# Van entre parentesis () y NO se pueden modificar (son inmutables)
tupla = ("Carlos", 25, "H", True)
print(tupla)
# Nota: Si intentamos hacer tupla[0] = "Otro", dara error


# CONJUNTOS (SETS)
# Van entre llaves {}, no tienen un orden fijo y no permiten datos repetidos
# ejemplo de conjunto
conjunto = {"Pedro", 22, 3}
print(conjunto)


# DICCIONARIOS
# Estructura de clave : valor, separados por comas
diccionario = {
    "nombre": "Pedro",
    "apellido": "Benites",
    "edad": 22
}

# Para acceder al valor se usa la clave (key) entre corchetes
print(diccionario["edad"]) # Imprimira 22