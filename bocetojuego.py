import random

deportes = ["1. ¿Quién fue el máximo goleador del Mundial Italia 1990? ", "2. ¿Cuántos Balones de Oro ha ganado Lionel Messi? ", "3. ¿Cuántos anillos de campeón logró Michael Jordan en la NBA? "]
opciones_deportes = [
    ["a. Gaetano Scirea", "b. Hristo Stoichkov", "c. Salvatore Schillaci", "d. Neymar"],
    ["a. 9", "b. 8", "c. 7", "d. 4"], 
    ["a. 6", "b. 5", "c. 11", "d. 3"]
]
respuestas_deportes = ["c", "b", "a"]

musica = []
opciones_musica = []
respuestas_musica = []

historia = []
tecnologia = []

puntos = []
jugadores = []
CATEGORIAS = [deportes, musica, historia, tecnologia]

CANTIDAD_PREGUNTAS = 3



#* Poner límite de jugadores
#* Pasear a los jugadores por varias categorias, mostrar cuantos puntos sacaron en cada una
#* La respuesta a la preguna puede estar en la última posicion de las opciones, para tener menos arrays
#* Las preguntas se pueden suprimir de los arrays a nivel local para que no se repitan



#Crea un nuevo jugador y agrega su posición para calcular el puntaje
def inicializarJugador(jugadores):
    print("Jugador",len(jugadores) + 1)
    jugadores.append(input("Ingrese su nombre: "))
    puntos.append(0)
    print()


#Imprime una opción abajo de la otra
def imprimirOpciones(array):
    print()
    for i in range(len(array)):
        print(array[i])
    print()


#Devuelve las respuestas (array) según la categoria correspondiente
def obtenerRespuestas(categoria):
    # TODO - Agregar las opciones que faltan
    if categoria == 1:
        respuestas = respuestas_deportes
    else:
        respuestas = respuestas_musica

    return respuestas

#Devuelve el array de opciones según la categoria ingresada
def obtenerOpciones(categoria):
    # TODO - Agregar las opciones que faltan
    if categoria == 1:
        preguntas = opciones_deportes
    else:
        preguntas = opciones_musica
    
    return preguntas

#Valida que el input esté en alguno de los valores del array
def validar(input, array):
    validado = False
    i = 0

    while not validado and i < len(array):
        if(array[i] == input):
            validado = True
        i += 1

    return validado


def jugar(indexCategoria,jugadores,puntos):
    contador = 0
    opciones = obtenerOpciones(indexCategoria)
    respuestas = obtenerRespuestas(indexCategoria)

    while contador < CANTIDAD_PREGUNTAS:
        print(CATEGORIAS[indexCategoria - 1][contador]) #Imprime la pregunta
        imprimirOpciones(opciones[contador]) #Imprime las opciones

        respuesta = input("Elige una de las opciones (a,b,c,d): ")

        while not validar(respuesta,['a','b','c','d']):
            respuesta = input("Opción incorrecta, intente nuevamente: ")
            
        print()

        if respuesta == respuestas[contador]:
            print("Respuesta correcta")
            puntos[len(jugadores) - 1] += 1
        else:
            print("Respuesta incorrecta")
        
        print("Puntos:", puntos[len(jugadores) - 1])

        print()
        contador += 1



# TODO - Poner en un while y que siga preguntando por mas jugadores
print("Bienvenido/a a Juego. Puedes elegir una de cuatro categorías temáticas o dejar que el juego escoja una al azar.")
inicializarJugador(jugadores)

print("Tendrás cinco preguntas para responder. ¡Mucha suerte!")

imprimirOpciones(["1. Deportes",'2. Música','3. Historia','4. Tecnología','5. Selección al azar'])
categoria = int(input("Ingresa tu opción: "))

while not validar(categoria,[1,2,3,4,5]):
    categoria = int(input("Opción incorrecta, intente nuevamente: "))

jugar(categoria,jugadores,puntos)
