# APUNTES: Condicionales anidados (if dentro de if) y elif

# Ejemplo de entrada de datos con decimales
ingreso_mensual = float(input("Ingresa tu sueldo mensual: "))
gasto_mensual = float(input("Ingresa tu gasto mensual: "))

print("--- RESULTADO DEL ANALISIS ---")

# Ejemplo de condicional principal
if ingreso_mensual >= 10000:
    print("Tienes un buen ingreso en cualquier pais")
    
    # Ejemplo de if anidado: Solo se lee si el ingreso es mayor a 10000
    if gasto_mensual <= 7000:
        print("Estas gastando correctamente")
    else:
        print("Estas gastando demasiado")

# elif: Se ejecuta solo si el primer if fue falso
elif ingreso_mensual >= 1000:
    print("Estas bien en latinoamerica")

elif ingreso_mensual >= 500:
    print("Estas bien economicamente en Argentina")

# else: Se ejecuta si ninguna condicion anterior se cumplio
else:
    print("Tienes ingresos bajos")