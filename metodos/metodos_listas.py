#List: crea una lista
lista =  list(['hola','jose',24])
lista2 = [7,3,6,4,2,7,4,8,9,10,False]
print(lista)

#len: se usa para contar los elementos de la lista

cantidad_elementos = len(lista)
print(cantidad_elementos) #3

#append: agregando elementos a la lista
lista.append("JAJAJ")
print(lista)

#insert: agrega un elemento a la lista en un índice específico
lista.insert(2,"pepe")#primer parámetro posición del índice, segundo parámetro: lo que agregará
print(lista)#si ya existe algo en la posición dos, simplemente lo recorre

#extend: agregando varios elementos a la lista
lista.extend(["pepe",20,23])#se tienen que poner los corechetes
print(lista)
    
#pop: eliminando un elemento de una lista

print(len(lista))
lista.pop(0)
print(len(lista)) #checamos que tiene un elemento menos

lista.pop(-1)#para eliminar el ultimo elemento, -1 para el ultimo, -2 para el penultimo y así sucesivamente
print(lista)
#remove: removiendo por su valor
lista.remove(20)
print(lista)

#clear: elimina todos los elementos de la lista 
#lista.clear()
#print(lista)

#sort: ordena de forma ascendente pero este no sirve con cadenas de texto
lista2.sort()
print(lista2)
#para ordenarlos de forma descendente es lista2.sort(reverse = True)

#reverse: la lista original la voltea, no ordena solo voltea, esta si acepta todo tipo de caracteres
lista.reverse()
print(lista)

#para ver todos los métodos de lista
print(dir(lista))
#para ver los métodos de una tupla
print(dir(('aaa','aaaa')))
#cada tipo de dato tiene diferentes métodos

