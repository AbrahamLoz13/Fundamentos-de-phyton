# Objetivo del problema:
# Validar el acceso a una atracción mediante requisitos dobles (estatura y edad)
# utilizando estructuras condicionales anidadas para dar respuestas específicas.

altura = 130
edad = 1

# Resolución - Validación por niveles:

# #ejemplo de condicional anidado
# El objetivo del primer nivel es filtrar por el requisito físico de altura.
if altura >= 120:
    # El objetivo del segundo nivel es filtrar por el requisito legal de edad.
    # Este bloque solo se ejecuta si la condición de altura fue verdadera.
    if edad >= 18:
        print("puedes pasar")
    else:
        # Respuesta específica si cumple altura pero no edad.
        print("no puedes pasar eres menor de edad")

else: 
    # Respuesta directa si no cumple el primer requisito (altura).
    print("no puedes pasar eres muy chaparro")