#For: sirve para iteraciones, en estre ejemplo lo que va a hacer es que va a iterar
#toda la lista elemento por elemento

animales = ["perro","gato","gallo","puerco"]
numeros = [1,2,3,4,]
for iterar_animal in animales:
    print(iterar_animal)
    
    
    
#cada numero iterado se multiplicará por 10   

for numero in numeros:
    resultado = numero * 10
    print(resultado)

#hay una forma de iterar 2 listas O MAS, de requisito es 
#que las listas tengan la misma cantidad de elementos

for iterar_animal,numero in zip(animales, numeros):
    print(f"lista 1: {iterar_animal}")    
    print(f"lista 2: {numero}")    
    
    
#también podemos iterar con range, el primer parámetro es donde empieza y el ultimo donde ya se acabará
#cuando llegue a 10 ya no se imprimirá el 10 debido a que se cumplió la condición
for num in range(3,10):
    print(num)

#forma correcta de recorrer un numero con su indice
for num in enumerate(numeros):
    print(num)
    