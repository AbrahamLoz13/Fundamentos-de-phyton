# Objetivo del problema:
# Validar si un cliente cumple con tres requisitos independientes (lista VIP, edad y presupuesto) 
# mediante el uso de operadores de pertenencia (in) y comparadores lógicos.

# Configuración de requisitos
vip_list = ["Abraham", "Pepe", "Sofía"]
edad_minima = 18
precio = 50

# Datos del cliente
nombre_cliente = "Abraham"
edad_cliente = 17
dinero_cliente = 51

# Resolución - Evaluación de condiciones:

# #ejemplo de operador 'in'
# El objetivo es comprobar si el string existe dentro de la lista VIP
esta_en_lista = nombre_cliente in vip_list

# #ejemplo de operador de comparación mayor o igual
# El objetivo es verificar si el cliente alcanza la edad mínima requerida
es_mayor = edad_cliente >= edad_minima

# #ejemplo de comparación de valores numéricos
# El objetivo es asegurar que el cliente tiene suficiente dinero para pagar
tiene_dinero = dinero_cliente >= precio

# Resultados
print(esta_en_lista)
print(es_mayor)
print(tiene_dinero)