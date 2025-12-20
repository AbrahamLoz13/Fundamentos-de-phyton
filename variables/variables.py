# APUNTES: Variables, Concatenacion y Operadores de Pertenencia

# Tipado Dinamico: No es necesario declarar el tipo de variable
nombre = "Lucia"
print(nombre)

# ejemplo de operadores de asignacion
# Suma el valor a la variable existente
numero = 50
numero += 1 
print(numero)

# CONCATENACION (Unir textos)

# ejemplo de concatenacion con signo +
# Solo sirve para unir texto con texto
print("Hola " + nombre + ", bienvenida")

# ejemplo de concatenacion con f-strings (Recomendada)
# Permite incrustar variables directamente dentro de las llaves {}
saludo = f"Hola {nombre}, saludos"
print(saludo)

# f-strings convierte automaticamente numeros o booleanos a texto
es_valido = True
mensaje = f"El estado es: {es_valido}"
print(mensaje)


# OPERADORES DE PERTENENCIA (in / not in)

# Verifican si un valor existe dentro de una variable
# Es sensible a mayusculas y minusculas
titulo = "Curso de Python"

print("Python" in titulo)     # True
print("Java" not in titulo)   # True