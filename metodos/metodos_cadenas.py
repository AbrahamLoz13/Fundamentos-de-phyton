# APUNTES: Metodos de cadenas (Strings)

cadena1 = "hola soy Pepe"
cadena2 = "12345"

# dir: Devuelve la lista de atributos y metodos validos del objeto
# Es util para ver que se puede hacer con un tipo de dato
resultado = dir(cadena1)

# NOTA: Para ejecutar los metodos se deben usar parentesis ()

# upper: Convierte todo el texto a mayusculas
mayus = cadena1.upper()
print(mayus)

# lower: Convierte todo el texto a minusculas
minus = cadena1.lower()
print(minus)

# capitalize: Convierte solo la primera letra a mayuscula
primera_mayus = cadena1.capitalize()
print(primera_mayus)

# find: Busca una cadena dentro de otra
# Devuelve la posicion (indice) donde empieza
# Si NO encuentra el valor, devuelve -1
busqueda_find = cadena1.find("hola")
print(busqueda_find)

# index: Igual que find, pero si NO encuentra el valor lanza un error (excepcion)
busqueda_ind = cadena1.index("hola")
print(busqueda_ind)

# isnumeric: Devuelve True si la cadena contiene solo numeros
es_numerico = cadena2.isnumeric()
print(es_numerico)

# isalpha: Devuelve True si son solo letras (a-z)
# Los espacios y caracteres especiales hacen que de False
es_texto = cadena1.isalpha()
print(es_texto)

# count: Cuenta cuantas veces aparece una letra o palabra en la cadena
contar_cadena = cadena1.count("a")
print(contar_cadena)

# len: Cuenta la cantidad total de caracteres (incluyendo espacios)
# NOTA: len es una funcion, no un metodo
contar_caracteres = len(cadena1)
print(contar_caracteres)

# startswith: Verifica si la cadena empieza con el texto indicado
# Devuelve True o False
inicia_con = cadena1.startswith("h")
print(inicia_con)

# endswith: Verifica si la cadena termina con el texto indicado
# Devuelve True o False
termina_con = cadena1.endswith("m")
print(termina_con)

# replace: Reemplaza un fragmento de texto por otro
# Primer parametro: valor antiguo, Segundo parametro: valor nuevo
cadena_nueva = cadena1.replace("la", "lu")
print(cadena_nueva) # ejemplo de resultado: holu soy pepe

# split : separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(" ")#nos va a separar por cada espacio y nos devuelve una matriz (lista)
print(cadena_separada)# ['hola','soy','pepe']
