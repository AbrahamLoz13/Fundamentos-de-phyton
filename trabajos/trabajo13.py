# Objetivo del problema:
# Aplicar un aumento salarial condicionado mediante un código promocional, 
# validando simultáneamente la vigencia del código y el nivel de ingresos del usuario.

# #ejemplo de casting a entero
salario = int(input("Ingrese su salario: "))
codigo = input("Ingrese el código: ")

# Resolución - Validación y cálculo:

# #ejemplo de normalización de entrada
# El objetivo es que el código funcione sin importar las mayúsculas (ej: "PYTHON20").
codigo_valido = codigo.lower()

# #ejemplo de operador lógico 'and'
# El objetivo es verificar dos requisitos: que el código sea correcto Y que el sueldo sea bajo.
if codigo_valido == "python20" and salario < 2000:
    # #ejemplo de cálculo de porcentaje
    # El objetivo es sumar el 10% al salario original.
    salario_descuento = salario + (salario * .10) 
    print(f"Descuento aplicado, su nuevo sueldo es {salario_descuento}")

# #ejemplo de condición excluyente con elif
# El objetivo es detectar casos donde el código es correcto pero no cumple el criterio de salario.
elif codigo_valido == "python20" and salario >= 2000:
    print("Codigo válido pero ya ganas bien, no seas hambreado")

else:
    # El objetivo es capturar cualquier código que no sea "python20".
    print("Código inválido")