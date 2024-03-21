from random import choice
from turtle import *
from freegames import floor, vector

# Se inicia el state (diccionario) con una llave llamada score que tiene valor 0
state = {'score': 0} #el puntaje inicia en 0 y aumenta

#camino que sigue el pacman
path = Turtle(visible=False)
writer = Turtle(visible=False)

#direcccion en la que se mueve el pacman
aim = vector(5, 0)

#coordenada inicial donde se encuentra pacman
pacman = vector(-25, -40)

#posicion inicial donde se encuentran los fantasmas
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -120), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -120), vector(-5, 0)],
]

# tablero
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# Funcion que pinta los cuadros azules, (x, y)
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

# Funcion que devuelve el desplazamiento del punto, punto
def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

# Funcion que regresa true si el punto es valido, punto
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

# Funcion que dibuja la cuadricula del juego 
def world():
    "Draw world using path."
    bgcolor('black') #color de fondo
    path.color('blue') # color del camino

	#indice en el rango del tablero 
    for index in range(len(tiles)):
        tile = tiles[index] # a esta variable se le agrega el valor del tablero en la posicion

        if tile > 0:
            x = (index % 20) * 20 - 200 # x toma el valor del indice (modulo de 20 x 20 - 200)
            y = 180 - (index // 20) * 20 # y toma el valor de 180 - el indice // 20 y despues * 20 (// division entera)
            square(x, y) #manda a llamar la funcion square

            if tile == 1:
                path.up() #el camino sube
                path.goto(x + 10, y + 10) # a x,y se le suman 10 cada uno
                path.dot(2, 'white') 

# Funcion que define el movimiento de pacman y los fantasmas
def move():
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)

        else: #los ciclos if definen la inteligencia de los fantasmas ademas que aumentan la velocidad de los fantasmas
            if pacman.x > point.x and pacman.y > point.y:
                options = [
                    vector(10, 0),
                    vector(10, 0),
                    vector(10, 0),
                    vector(-10, 0),
                    vector(0, 10),
                    vector(0, 10),
                    vector(0, 10),
                    vector(0, -10),
                ]

            elif pacman.x < point.x and pacman.y >point.y:
                options = [
                    vector(10, 0),
                    vector(-10, 0),
                    vector(-10, 0),
                    vector(-10, 0),
                    vector(0, 10),
                    vector(0, 10),
                    vector(0, 10),
                    vector(0, -10),
                ]

            elif pacman.x > point.x and pacman.y < point.y:
                options = [
                    vector(10, 0),
                    vector(10, 0),
                    vector(10, 0),
                    vector(-10, 0),
                    vector(0 ,10),
                    vector(0, -10),
                    vector(0, -10),
                    vector(0, -10),
                ]
            
            elif pacman.x < point.x and pacman.y < point.y:
                options = [
                    vector(10, 0),
                    vector(-10, 0),
                    vector(-10, 0),
                    vector(-10, 0),
                    vector(0, 10),
                    vector(0, -10),
                    vector(0, -10),
                    vector(0, -10),
                ]

            else:
                options = [
                    vector(5,0),
                    vector(-5, 0),
                    vector(0, 5),
                    vector(0, -5),
                ]


            plan = choice(options) #se elije un fantasma para mover
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

	#cuando pacman se encuentra a un fantasma no deja que pase
    for point, course in ghosts:
        if abs(pacman - point) < 25: # 20
            return

    ontimer(move, 50) #100

# funcion que cambia la direccion de pacman con las coordenadas recibidas, (x,y)
def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

setup(420, 420, 370, 0) #tamaño de la ventana
hideturtle()
tracer(False)
writer.goto(160, 160) #escribe posicion
writer.color('white') #color de los puntos
writer.write(state['score']) # puntaje del jugador
listen()

#cambia la direccion en la que se mueve pacman
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
