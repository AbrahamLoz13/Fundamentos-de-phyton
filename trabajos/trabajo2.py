#Nivel 2: La Ficha del Jugador (Lógica)
#Escribe un programa desde cero que haga lo siguiente (usa variables para todo):

#Crea una variable puntos_vida con valor 100.

#El jugador recibe un golpe: Réstale 15 a puntos_vida (usa el operador de resta o -=).

#El jugador encuentra una poción: Súmale 20 a puntos_vida.

#Crea una lista llamada inventario que tenga: "Espada", "Escudo", "Mapa".

#Imprime un mensaje final usando f-string que diga algo como:

#"El jugador tiene X puntos de vida y lleva un Escudo en su inventario." 
# (Tip: Para imprimir "Escudo", accede al elemento correcto de tu lista).

puntos_vida = 100

golpe = puntos_vida - 15

puntos_vida = golpe + 20


inventario = ["Espada","Escudo","Mapa"]

print(f"El jugador tiene {puntos_vida} puntos y lleva un {inventario[1]} en su inventario")