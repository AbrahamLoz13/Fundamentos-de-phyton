#creando un conjunto con set

conjunto = set(["Dato1","Dato2"])

print(conjunto)
#recordemos que con set no se pueden modificar datos

#una manera de poner un conjunto de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)

#teoria de conjutos

conjunto3 = {1,3,5,7}
conjunto4 = {1,3,5}

#verificando si es un subconjunto
resultado = conjunto4.issubset(conjunto3)
print(resultado)
