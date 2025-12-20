edad_texto = input("Dime tu edad: ")


if edad_texto.isnumeric():
    
    edad_in = int(edad_texto)
    if edad_in >= 18:
        print("eres mayor de edad")
    else:
        print("eres menor de edad")
        
else:
    
    print("por favor escriba numeros solamente")
    