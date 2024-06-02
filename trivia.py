import random

deportes = ['¿Quién fue el máximo goleador del Mundial Italia 1990?', '¿Cuántos Balones de Oro ha ganado Lionel Messi?', '¿Cuántos anillos de campeón logró Michael Jordan en la NBA?', '¿A quién le pertenece el récord de más victorias en el Masters de Augusta de golf?', '¿Qué equipo ha ganado más Stanley Cups en la NHL?', '¿Quién ganó el Campeonato Mundial de Pilotos de Fórmula 1 2016?', '¿En qué año los New Orleans Saints ganaron el Super Bowl?', '¿Quién es el jugador japonés con más hits de por vida en la MLB?', '¿Cuántos Abiertos de Francia ganó Björn Borg?', '¿Quién es el máximo goleador de la selección de fútbol de Inglaterra?']
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

musica = ['¿"Unison" de Björk contiene una muestra de qué canción de Oval?', '¿Artis Leon Ivey Jr. es más conocido como qué artista de rap?', '¿Cuál fue el álbum debut de Rage Against the Machine?', '¿Qué banda grabó el álbum "Parallel Lines"?', '¿Quién es el letrista principal de la banda canadiense de rock progresivo Rush?', '¿Cuál es el nombre artístico de la cantante neozelandesa Phillipa "Pip" Brown?', '¿Cuántas cuerdas hay en un violonchelo?', '¿Con qué famoso guitarrista colaboró Pete Townshend para un evento en la Academia Brixton en 1985?', '¿"Drink the Sea" es un álbum de qué artista de música electrónica?', 'En 2006, ¿qué banda lanzó su álbum debut "A Fever You Can’t Sweat Out"?']
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

historia = ['¿Cómo era más conocido William Frederick Cody?', '¿Quién fue el presidente de Argentina en 1939?', '¿Dónde se libró la Segunda Guerra Bóer en 1899?', '¿Cuándo empezó la Guerra de la Independencia contra el imperio francés?', '¿Cómo se llamaba la operación ofensiva alemana realizada en octubre de 1941 para tomar Moscú antes del invierno?', '¿En 1939, Gran Bretaña y Francia declararon la guerra a Alemania después de invadir qué país?', '¿Cuántas veces se casó Albert Einstein en su vida?', '¿Cuándo comenzó la Revolución Francesa?', '¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?', '¿En qué año se fundó Canadá?']
opciones_historia = [
    ['a. Billy The Kid', 'b. Buffalo Bill', 'c. Pawnee Bill', 'd. Wild Bill Hickok'],
    ['a. Roberto Marcelino Ortiz', 'b. Agustín Pedro Justo', 'c. Hipólito Yrigoyen', 'd. Ramón Castillo'],
    ['a. Argentina', 'b. Nepal', 'c. Bulgaria', 'd. Sudáfrica'],
    ['a. 1808', 'b. 1810', 'c. 1809', 'd. 1806'],
    ['a. Operación Girasol', 'b. Operación Barbarroja', 'c. Case Blue', 'd. Operación Typhoon'],
    ['a. Estonia', 'b. Austria', 'c. Polonia', 'd. Hungría'],
    ['a. Cinco veces', 'b. Dos veces', 'c. Una vez', 'd. Tres veces'],
    ['a. 1789', 'b. 1756', 'c. 1799', 'd. 1823'],
    ['a. 1775', 'b. 1774', 'c. 1777', 'd. 1776'],
    ['a. 1798', 'b. 1867', 'c. 1668', 'd. 1859']
]
respuestas_historia = ["b", "a", "d", "a", "d", "c", "b", "a", "d", "b"]

peliculas = ['¿Cuál es la frase correcta para el dicho latino "Romanes Eunt Domus" en "La Vida de Brian" de Monty Python?', '¿Quién dirigió las películas "Pulp Fiction", "Reservoir Dogs" y "Django Unchained"?', '¿Cuál fue otro nombre sugerido para la película de 1985 "Volver al Futuro"?', '¿Cuál de estas películas NO está ambientada en Los Ángeles?', '¿Qué película de 1958 fue protagonizada por Kirk Douglas y Tony Curtis como los medio hermanos Einar y Eric?', 'En "Buscando a Nemo", ¿cómo se llamaba la madre de Nemo?', 'En "Volver al Futuro II", ¿a qué fecha futura acuden Marty y el Dr. Emmett Brown?', '¿Quién interpretó a Batman en la película de 1997 "Batman and Robin"?', '¿Cuál de los siguientes actores no desempeña un papel en la película "The Usual Suspects"?', '¿Cuál es la película más antigua de Disney?']
opciones_peliculas = [
    ['a. Romans Go Home', 'b. Romani Ite Domum', 'c. Yomate Istis Homem', 'd. Romani Itei Domus'],
    ['a. Martin Scorsese', 'b. Steven Spielberg', 'c. Quentin Tarantino', 'd. James Cameron'],
    ['a. Hombre del espacio de Plutón', 'b. Un viaje en el tiempo', 'c. El hombre afortunado', 'd. Viajeros en el tiempo de Hill Valley'],
    ['a. RoboCop', 'b. Terminator', 'c. Predator 2', 'd. Blade Runner'],
    ['a. Los barcos largos', 'b. Los vikingos', 'c. Espartaco', 'd. Príncipe Valiente'],
    ['a. Arenosa', 'b. Perla', 'c. Coral', 'd. Leia'],
    ['a. 13 de julio de 2015', 'b. 20 de julio de 2015.', 'c. 25 de enero de 2015', 'd. 21 de octubre de 2015'],
    ['a. Michael Keaton', 'b. Val Kilmer', 'c. Christian Bale', 'd. George Clooney'],
    ['a. Steve Buscemi', 'b. Benicio Del Toro', 'c. Gabriel Byrne', 'd. Kevin Spacey'],
    ['a. Pinocho', 'b. Blancanieves', 'c. Fantasía', 'd. Dumbo']    
]
respuestas_peliculas = ["b", "c", "a", "a", "b", "c", "d", "d", "a", "b"]

NOMBRES_CATEGORIAS = ["Deportes","Música","Historia","Películas"]
puntos = []
jugadores = []
CATEGORIAS = [deportes, musica, historia, peliculas]

TOTAL_PREGUNTAS = 10
CANTIDAD_PREGUNTAS = 5
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

#Imprime una categoría a la vez entre las que están disponibles
def imprimirCategorias(control_categorias):
    strings_categorias = ["", "1. Deportes", "2. Música", "3. Historia", "4. Películas", "5. Selección al azar"]
    for i in range(1, len(strings_categorias)):
        contador = 0
        while contador < len(control_categorias) and i != control_categorias[contador]:
            contador += 1
        if contador < len(control_categorias):
            print(strings_categorias[i])
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
        opciones = opciones_deportes
    elif categoria == 2:
        opciones = opciones_musica
    elif categoria == 3:
        opciones = opciones_historia
    else:
        opciones = opciones_peliculas
    
    return opciones

#Valida que el input esté en alguno de los valores del array
def validar(input, lista):
    validado = False
    i = 0

    while not validado and i < len(lista):
        if(lista[i] == input):
            validado = True
        i += 1

    return validado

#Genera lista de indices random para las preguntas a mostrar
def crearIndicesRandom(CANTIDAD_PREGUNTAS, TOTAL_PREGUNTAS):
    lista_random = []
    contador = 0
    while contador < CANTIDAD_PREGUNTAS:
        numero_random = random.randint(0,TOTAL_PREGUNTAS-1)
        i = 0
        while i < len(lista_random) and numero_random != lista_random[i]:
            i += 1
        if i >= len(lista_random):
            lista_random.append(numero_random)
            contador += 1
    return lista_random


#Verifica que al usar la opción random se elija una categoría disponible
def asignarRandom(categoria, control_categorias):
    indice = random.randint(0, len(control_categorias) - 1)
    while control_categorias[indice] == CAT_RANDOM:
        indice = random.randint(0, len(control_categorias) - 1)
    categoria = control_categorias[indice]
    return categoria

#Verifica cuáles categorías le faltan por jugar al usuario
def controlarCategorias(categoria, control_categorias):
    i = 0
    largo = len(control_categorias)
    while i < largo and control_categorias[i] != categoria:
        i += 1          
    if categoria == control_categorias[i]:
        del control_categorias[i]
    return control_categorias


def jugar(indexCategoria,jugadores,puntos):
    contador = 0
    #Agregué esta línea
    lista_random = crearIndicesRandom(CANTIDAD_PREGUNTAS, TOTAL_PREGUNTAS)
    opciones = obtenerOpciones(indexCategoria)
    respuestas = obtenerRespuestas(indexCategoria)

    print('--------------------------------------------------')
    print("Categoría:",NOMBRES_CATEGORIAS[indexCategoria - 1])

    while contador < CANTIDAD_PREGUNTAS:
        print('--------------------------------------------------')
        print(CATEGORIAS[indexCategoria - 1][(lista_random[contador])]) #Imprime la pregunta recorriendo los índices de la lista random, y con el mismo contador mantiene el orden hasta el final 
        imprimirOpciones(opciones[(lista_random[contador])]) #Imprime las opciones correspondientes a la pregunta random, con el mismo contador hasta el final

        respuesta = input("Elige una de las opciones (a, b, c, d): ")

        while not validar(respuesta,['a','b','c','d']):
            respuesta = input("Opción incorrecta, intente nuevamente: ")
            
        print('--------------------------------------------------')

        if respuesta == respuestas[(lista_random[contador])]:#Revisa las respuestas correspondientes a la pregunta random, con el mismo contador
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
    print()


#Programa principal
continuar = True
while continuar:
    print('--------------------------------------------------')
    print()
    print("Bienvenido a T.P.O (Trivia Program Online).")
    print()
    print("Tendrás que responder preguntas en cuatro categorías temáticas para completar el juego. En cada ronda podrás elegir la categoría que deseas enfrentar en ese momento o dejar que el sistema escoja una al azar.")

    inicializarJugador(jugadores)

    print("Tendrás", CANTIDAD_PREGUNTAS, "preguntas para responder. ¡Mucha suerte!")
    print()

    contador_categorias = 0
    control_categorias = [1, 2, 3, 4, 5]

    #Ciclo de cada jugador
    while contador_categorias < len(CATEGORIAS):
        print('--------------------------------------------------')
        imprimirCategorias(control_categorias)
        categoria = int(input("Ingresa tu opción: "))
        
        while not validar(categoria, control_categorias):
            categoria = int(input("Opción incorrecta, intente nuevamente: "))

        if categoria == CAT_RANDOM:
            categoria = asignarRandom(categoria, control_categorias)

        jugar(categoria,jugadores,puntos)
        
        control_categorias = controlarCategorias(categoria, control_categorias)             
        contador_categorias +=1

    if len(jugadores) < MAX_JUGADORES:
        seguir = int(input("¿Desea ingresar otro jugador? Presione 1 para ingresarlo o presione 2 para terminar el juego: "))
        while seguir != 1 and seguir != 2:
            seguir = int(input("Por favor, indique la opción correcta. Presione 1 para ingresarlo o presione 2 para terminar el juego: "))
        if seguir == 2:
            continuar = False
    else:
        print("Han llegado al máximo de jugadores para esta partida")
        continuar = False


mostrarPuntaje(jugadores,puntos)