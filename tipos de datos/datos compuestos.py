
#LISTA

#ejemplo simple de una lista

lista = ["Abraham","21151097",9,True]
print(lista)
#para seleccionar solo un item de la lista se cuenta del 0 al 9

lista2 = ["Jafet","H",9,False]
lista2[0] = "Pepe"
print(lista2[0])#imprimirá PEPE ya que se puede modificar
print(lista2[1])#imprimirá H    
print(lista2[2])#imprimirá 9
print(lista2[3])#imprimirá False

#TUPLAS

#es como lista pero envés de [] se usa ()
#a diferencia de la lista, la dupla no se puede modificar

tupla = ("Pepito",22,"H", False)
print(tupla)
#Conjunto

conjunto = {"pepe",22,3}

#Diccionario, se separa por comas

diccionario = {
    "Nombre":"Abraham",
    "Apellido":"Lozano",
    "Edad": 22
}

print(diccionario["Edad"])#Me va a mostrar la edad de mi diccionario osea 22
