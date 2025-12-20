#Dir: devuelve la lista de atributos validos del objeto pasado
#es para ver todos los métodos de algo

cadena1 = "hola soy Abraham"
cadena2 = "12345"

resultado = dir(cadena1)

#PARA LOS MÉTODOS SE DEBE DE USAR ()


#UPER: convierte todo a mayúsculas
mayus = cadena1.upper()
print(mayus)
#LOWER: convierte todo a minúsculas
minus = cadena1.lower()
print(mayus)
#CAPITALIZE: convierte la primera en mayúscula
primera_mayus = cadena1.capitalize()
print(primera_mayus)

#FIND: Buscar un texto dentro de una cadena

busqueda_find = cadena1.find("hola") #en esta línea va a buscar el texto hola en la cadena uno

print(busqueda_find)#lo que me da es la posición de el texto o letra buscada en la cadena
#cuando no encuentra un valor nos devuelve -1


#INDEX: a diferencia de esta no nos da -1, nos da un error (exception), lo demás es igual
busqueda_ind = cadena1.index("hola") #en esta línea va a buscar el texto hola en la cadena uno

print(busqueda_ind)#lo que me da es la posición de el texto o letra buscada en la cadena
#cuando no encuentra un valor nos devuelve -1

#IS NUMERIC: si es numérico devolvemos true, si no es false
es_numerico = cadena2.isnumeric()
print(es_numerico)

#ES ALPHANUMERICO: si son letras de la "a" a la "z" devuelve true, sin caracteres especiales ni espacios
es_texto = cadena1.isalpha()
print(es_texto)

#COUNT: cuenta las letras o palabras dentro de una cadena
contar_cadena = cadena1.count("a")#va a contar las "a"
print(contar_cadena)

#LEN: cuenta la cantidad de carácteres de una cadena dentro de otra cadena

contar_coincidencias = len(cadena1) #ESTE NO ES UN MÉTODO ES UNA FUNCIÓN
print(contar_coincidencias)#me devuelve la cantidad de carácteres de el texto

#STARTSWITHverifica si una cadena empieza con lo indicado por nosotros
inicia_con = cadena1.startswith("a")
print(inicia_con)#si inicia con a devuelve true si no, false, respetando


#ENDWITHverifica si una cadena termina con lo indicado por nosotros
termina_con = cadena1.endswith("a")
print(termina_con)#si termina con a devuelve true si no, false, respetando

#REPLACE: remplaza un texto por otro, en el primer parámetro ponemos lo que queremos remplazar por el segundo
cadena_nueva = cadena1.replace("la","lu")
print(cadena_nueva)#nos daría holu soy abraham
