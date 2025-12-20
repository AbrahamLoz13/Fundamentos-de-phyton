
#en lenguajes como phyton no es necesario estsblecer el tipo de variable
#ya que este es un lenguaje dinámico por ejemplo

nombre = "Abraham"
print(nombre)
#en cuestión de los números, si pones que numero = 10 y luego pones número += 1, se le va a sumas 1 al 10
numero = 10
numero += 1
print(numero)

#concatenar: unir cadenas de texto, en este ejemplo imprimirá: Hola Jafet ¿Cómo estás?

#CONCATENAR CON +

print("Hola " +nombre+ " ¿Cómo estás?")

#CONCATENAR CON F

bienvenida = f'Hola {nombre} ¿Cómo estás?'
print(bienvenida)

#CONCATERNAR CON F NUMEROS O BOOLEANS A TEXTO

#una de la ventaja que tiene esta forma de concatenar es que puede convertir números a texto'''

boolean = False
cadena = f"es {boolean}"
print(cadena)

#OPERADORES DE PERTENENCIA IN/ NOT IN

#podemos buscar el texto que tiene una variable con el siguiente ejemplo, si lo que buscamos si se encuentra
#retornará un true, de lo contrario será false, esto es sensible con mayúsculas y minúsculas'''

apellido = "Abraham"
print("Abraham" in apellido)#true
print("Abraham" not in apellido)#false


