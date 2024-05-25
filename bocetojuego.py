import random

deportes = ['1. ¿Quién fue el máximo goleador del Mundial Italia 1990?', '2. ¿Cuántos Balones de Oro ha ganado Lionel Messi?', '3. ¿Cuántos anillos de campeón logró Michael Jordan en la NBA?', '4. ¿A quién le pertenece el récord de más victorias en el Masters de Augusta de golf?', '5. ¿Qué equipo ha ganado más Stanley Cups en la NHL?', '6. ¿Quién ganó el Campeonato Mundial de Pilotos de Fórmula 1 2016?', '7. ¿En qué año los New Orleans Saints ganaron el Super Bowl?', '8. ¿Quién es el jugador japonés con más hits de por vida en la MLB?', '9. ¿Cuántos Abiertos de Francia ganó Björn Borg?', '10. ¿Quién es el máximo goleador de la selección de fútbol de Inglaterra?']
opciones_deportes = [
    ['a. Gaetano Scirea', 'b. Hristo Stoichkov', 'c. Salvatore Schillaci', 'd. Neymar'],
    ['a. 9', 'b. 8', 'c. 7', 'd. 4'], 
    ['a. 6', 'b. 5', 'c. 11', 'd. 3'],
    ['a. Jack Nicklaus', 'b. Gary Player', 'c. Tiger Woods', 'd. Jordan Spieth'],
    ['a. Chicago Blackhawks', 'b. Toronto Maple Leafs', 'c. Detroit Red Wings', 'd. Montréal Canadiens'],
    ['a. Lewis Hamilton', 'b. Max Verstappen', 'c. Kimi Raikkonen', 'd. Nico Rosberg'],
    ['a. 2008', 'b. 2009', 'c. 2011', 'd. 2010'],
    ['a. Shohei Ohtani', 'b. Hideki Matsui', 'c. Ichiro Suzuki', 'd. Kazuo Matsui'],
    ['a. 4', 'b. 9', 'c. 2', 'd. 6'],
    ['a. David Beckham', 'b. Harry Kane', 'c. Michael Owen', 'd. Wayne Rooney']
]
respuestas_deportes = ['c', 'b', 'a', 'a', 'd', 'd', 'd', 'c', 'd', 'b']

musica = ['1. ¿"Unison" de Björk contiene una muestra de qué canción de Oval?', '2. ¿Artis Leon Ivey Jr. es más conocido como qué artista de rap?', '3. ¿Cuál fue el álbum debut de Rage Against the Machine?', '4. ¿Qué banda grabó el álbum "Parallel Lines"?', '5. ¿Quién es el letrista principal de la banda canadiense de rock progresivo Rush?', '6. ¿Cuál es el nombre artístico de la cantante neozelandesa Phillipa "Pip" Brown?', '7. ¿Cuántas cuerdas hay en un violonchelo?', '8. ¿Con qué famoso guitarrista colaboró Pete Townshend para un evento en la Academia Brixton en 1985?', '9. ¿"Drink the Sea" es un álbum de qué artista de música electrónica?', '10. En 2006, ¿qué banda lanzó su álbum debut "A Fever You Can’t Sweat Out"?']
opciones_musica = [
    ['a. Textuell', 'b. Aero Deck', 'c. do while', 'd. Panoramic'],
    ['a. Dr. Dre', 'b. Snoop Dogg', 'c. Coolio', 'd. Lil Wayne'],
    ['a. Evil Empire', 'b. Renegades', 'c. Battle of Los Angeles', 'd. Rage Against the Machine'],
    ['a. Paramore', 'd. Coldplay', 'c. The Police', 'd. Blondie'],
    ['a. Geddy Lee', 'b. Alex Lifeson', 'c. Neil Peart', 'd. John Rutsey'],
    ['a. Ladyhawke', 'b. Kesha', 'c. Anika Moa', 'd. Lorde'],
    ['a. 5', 'b. 6', 'c. 4', 'd. 8'],
    ['a. Jimmy Page', 'b. David Gilmour', 'c. Eric Clapton', 'd. Mark Knopfler'],
    ['a. Avicii', 'b. XXYYXX', 'c. Flux Pavilion', 'd. The Glitch Mob'],
    ['a. Panic! at the Disco', 'b. My Chemical Romance', 'c. Fall Out Boy', 'd. Twenty One Pilots']
]
respuestas_musica = ["b", "c", "d", "d", "c", "a", "c", "b", "d", "a"]

historia = ['1. ¿Cómo era más conocido William Frederick Cody?', '2. ¿Quién fue el presidente de Argentina en 1939?', '3. ¿Dónde se libró la Segunda Guerra Bóer en 1899?', '4. ¿Cuándo empezó la Guerra de la Independencia contra el imperio francés?', '5. ¿Cómo se llamaba la operación ofensiva alemana realizada en octubre de 1941 para tomar Moscú antes del invierno?', '6. ¿En 1939, Gran Bretaña y Francia declararon la guerra a Alemania después de invadir qué país?', '7. ¿Cuántas veces se casó Albert Einstein en su vida?', '8. ¿Cuándo comenzó la Revolución Francesa?', '9. ¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?', '10. ¿En qué año se fundó Canadá?']
opciones_historia = [
    ['a. Billy The Kid', 'b. Buffalo Bill', 'c. Pawnee Bill', 'd. Wild Bill Hickok'],
    ['Roberto Marcelino Ortiz', 'Agustín Pedro Justo', 'Hipólito Yrigoyen', 'Ramón Castillo'],
    ['Argentina', 'Nepal', 'Bulgaria', 'Sudáfrica'],
    ['1808', '1810', '1809', '1806'],
    ['Operación Girasol', 'Operación Barbarroja', 'Case Blue', 'Operación Typhoon'],
    ['Estonia', 'Austria', 'Polonia', 'Hungría'],
    ['Cinco veces', 'Dos veces', 'Una vez', 'Tres veces'],
    ['1789', '1756', '1799', '1823'],
    ['1775', '1774', '1777', '1776'],
    ['1798', '1867', '1668', '1859']
]
respuestas_historia = ["b", "a", "d", "a", "d", "c", "b", "a", "d", "b"]

peliculas = ['1. ¿Cuál es la frase correcta para el dicho latino "Romanes Eunt Domus" en "La Vida de Brian" de Monty Python?', '2. ¿Quién dirigió las películas "Pulp Fiction", "Reservoir Dogs" y "Django Unchained"?', '3. ¿Cuál fue otro nombre sugerido para la película de 1985 "Regreso al Futuro"?', '4. ¿Cuál de estas películas NO está ambientada en Los Ángeles?', '5. ¿Qué película de 1958 fue protagonizada por Kirk Douglas y Tony Curtis como los medio hermanos Einar y Eric?', '6. En "Buscando a Nemo", ¿cómo se llamaba la madre de Nemo?', '7. En "Regreso al Futuro II", ¿a qué fecha futura acuden Marty y el Dr. Emmett Brown?', '8. ¿Quién interpretó a Batman en la película de 1997 "Batman and Robin"?', '9. ¿Cuál de los siguientes actores no desempeña un papel en la película "The Usual Suspects"?', '10. ¿Cuál es la película más antigua de Disney?']
opciones_peliculas = [
    ['Romans Go Home', 'Romani Ite Domum', 'Yomate Istis Homem', 'Romani Itei Domus'],
    ['Martin Scorsese', 'Steven Spielberg', 'Quentin Tarantino', 'James Cameron'],
    ['Hombre del espacio de Plutón', 'Un viaje en el tiempo', 'El hombre afortunado', 'Viajeros en el tiempo de Hill Valley'],
    ['RoboCop', 'Terminator', 'Predator 2', 'Blade Runner'],
    ['Los barcos largos', 'Los vikingos', 'Espartaco', 'Príncipe Valiente'],
    ['Arenosa', 'Perla', 'Coral', 'Leia'],
    ['13 de julio de 2015', '20 de julio de 2015.', '25 de enero de 2015', '21 de octubre de 2015'],
    ['Michael Keaton', 'Val Kilmer', 'Christian Bale', 'George Clooney'],
    ['Steve Buscemi', 'Benicio Del Toro', 'Gabriel Byrne', 'Kevin Spacey'],
    ['Pinocho', 'Blancanieves', 'Fantasía', 'Dumbo']    
]
respuestas_peliculas = ["b", "c", "a", "a", "b", "c", "d", "d", "a", "b"]

NOMBRES_CATEGORIAS = ["Deportes","Música","Historia","Películas"]
puntos = []
jugadores = []
CATEGORIAS = [deportes, musica, historia, peliculas]

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
        respuestas = respuestas_peliculas

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
        preguntas = opciones_peliculas
    
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
    print("Bienvenido/a a T.P.O (Trivia Program Online). Puedes elegir una de cuatro categorías temáticas o dejar que el juego escoja una al azar.")

    inicializarJugador(jugadores)

    print("Tendrás cinco preguntas para responder. ¡Mucha suerte!")

    imprimirOpciones(["1. Deportes",'2. Música','3. Historia','4. Películas','5. Selección al azar'])
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