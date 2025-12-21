diccionario = {
    "nombre" : "Pepe",
    "apellido" : "Lopez",
    "edad": 25
    
}
#keys: devuelve las clases
claves = diccionario.keys()
print(claves)#me va a imprimir: ['nombre','apellido','edad']

#get: devuelve el valor, si no encuentra nada, el programa continúa

obtener = diccionario.get("nombre")
print(diccionario)

#pop: eliminamos un elemento de un diccionario
eliminar_elemento = diccionario.pop("apellido","nombre")#en caso de no existir apellido elimina el nombre
print(diccionario)

#clear: elimina todos los elementos de la lista
limpiar = diccionario.clear()

#obetiendo un elemento via items
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
