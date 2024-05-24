import random

deportes = ["1. ¿Quién fue el máximo goleador del Mundial Italia 1990? ", "2. ¿Cuántos Balones de Oro ha ganado Lionel Messi? ", "3. ¿Cuántos anillos de campeón logró Michael Jordan en la NBA? "]
opciones_deportes = [
    ["a. Gaetano Scirea", "b. Hristo Stoichkov", "c. Salvatore Schillaci", "d. Neymar"],
    ["a. 9", "b. 8", "c. 7", "d. 4"], 
    ["a. 6", "b. 5", "c. 11", "d. 3"]
]
respuestas_deportes = ["c", "b", "a"]

musica = ["Pregunta 1","Pregunta 2","Pregunta 3"]
opciones_musica = [
    ["a. Opción 1", "b. Opción 2", "c. Opción 3", "d. Opción 4"],
    ["a. Opción 1", "b. Opción 2", "c. Opción 3", "d. Opción 4"],
    ["a. Opción 1", "b. Opción 2", "c. Opción 3", "d. Opción 4"]
]
respuestas_musica = ["a","b","c"]

historia = ["Pregunta 1","Pregunta 2","Pregunta 3"]
opciones_historia = [
    ["a. Opción 1", "b. Opción 2", "c. Opción 3", "d. Opción 4"],
    ["a. Opción 1", "b. Opción 2", "c. Opción 3", "d. Opción 4"],
    ["a. Opción 1", "b. Opción 2", "c. Opción 3", "d. Opción 4"]
]
respuestas_historia = ["a","b","c"]

tecnologia = ["Pregunta 1","Pregunta 2","Pregunta 3"]
opciones_tecnologia = [
    ["a. Opción 1", "b. Opción 2", "c. Opción 3", "d. Opción 4"],
    ["a. Opción 1", "b. Opción 2", "c. Opción 3", "d. Opción 4"],
    ["a. Opción 1", "b. Opción 2", "c. Opción 3", "d. Opción 4"]
]
respuestas_tecnologia = ["a","b","c"]

NOMBRES_CATEGORIAS = ["Deportes","Música","Historia","Tecnología"]
puntos = []
jugadores = []
CATEGORIAS = [deportes, musica, historia, tecnologia]

CANTIDAD_PREGUNTAS = 3
MAX_JUGADORES = 5
CAT_RANDOM = len(CATEGORIAS) + 1 # Opción a seleccionar para que la categoria sea random


#Crea un nuevo jugador y agrega su posición para calcular el puntaje, verifica que el nombre de usuario no se repita
def inicializarJugador(jugadores):
    print()
    print("Jugador",len(jugadores) + 1)
    ocupado = True
    while ocupado:
        ocupado = False
        nombre = input("Ingrese un nombre de usuario: ")
        
        for i in range(len(jugadores)):
            if jugadores[i] == nombre:
                ocupado = True
                print("Ese nombre de usuario ya está en uso.")

    jugadores.append(nombre)
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
    if categoria == 1:
        respuestas = respuestas_deportes
    elif categoria == 2:
        respuestas = respuestas_musica
    elif categoria == 3:
        respuestas = respuestas_historia
    else:
        respuestas = respuestas_tecnologia

    return respuestas

#Devuelve el array de opciones según la categoria ingresada
def obtenerOpciones(categoria):
    if categoria == 1:
        preguntas = opciones_deportes
    elif categoria == 2:
        preguntas = opciones_musica
    elif categoria == 3:
        preguntas = opciones_historia
    else:
        preguntas = opciones_tecnologia
    
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

    print('--------------------------------------------------')
    print("Categoria:",NOMBRES_CATEGORIAS[indexCategoria - 1])

    while contador < CANTIDAD_PREGUNTAS:
        print('--------------------------------------------------')
        print(CATEGORIAS[indexCategoria - 1][contador]) #Imprime la pregunta
        imprimirOpciones(opciones[contador]) #Imprime las opciones

        respuesta = input("Elige una de las opciones (a,b,c,d): ")

        while not validar(respuesta,['a','b','c','d']):
            respuesta = input("Opción incorrecta, intente nuevamente: ")
            
        print('--------------------------------------------------')

        if respuesta == respuestas[contador]:
            print("Respuesta correcta")
            puntos[len(jugadores) - 1] += 1
        else:
            print("Respuesta incorrecta")
        
        print("Puntos:", puntos[len(jugadores) - 1])

        print()
        contador += 1

#Devuelve un array con los indices de los mejores puntajes
def mostrarPuntaje(jugadores,puntos):
    aux = 0

    #Ordenado de puntajes y jugadores
    for i in range(len(puntos)):
        for x in range(len(puntos)):
            if puntos[x] < puntos[i]:
                aux = puntos[x]
                puntos[x] = puntos[i]
                puntos[i] = aux

                aux = jugadores[x]
                jugadores[x] = jugadores[i]
                jugadores[i] = aux

    print()
    print("Tabla de posiciones:")

    for i in range(len(jugadores)):
        print((i + 1),"-",jugadores[i],"con",puntos[i],"puntos")


#Programa principal
continuar = True
while continuar:
    print()
    print("Bienvenido/a a Juego. Puedes elegir una de cuatro categorías temáticas o dejar que el juego escoja una al azar.")

    inicializarJugador(jugadores)

    print("Tendrás cinco preguntas para responder. ¡Mucha suerte!")

    imprimirOpciones(["1. Deportes",'2. Música','3. Historia','4. Tecnología','5. Selección al azar'])
    categoria = int(input("Ingresa tu opción: "))

    while not validar(categoria,[1,2,3,4,5]):
        categoria = int(input("Opción incorrecta, intente nuevamente: "))

    if categoria == CAT_RANDOM:
        categoria = random.randint(1,CAT_RANDOM - 1)

    jugar(categoria,jugadores,puntos)

    if len(jugadores) < MAX_JUGADORES:
        if int(input("¿Desea ingresar otro jugador? Presione 1: ")) != 1:
            continuar = False
    else:
        print("Han llegado al máximo de jugadores para esta partida")
        continuar = False


mostrarPuntaje(jugadores,puntos)