"""
   Actividad 5. Juego de Memoria
   Modificaciones:
    - Contar y desplegar el numero de taps
    - Detectar cuando todos los cuadros se han destapado
    - Centrar el dígito en el cuadro
    - Utilizar algo diferente a los dígitos para resolver el juego
"""

from random import *
from turtle import *
from freegames import path

# Se define la imagen que se utilizara
car = path('car.gif')

# Simbolos que se mostraran
tiles = ['$', '?', '¿', '@', '+', '*', '%', 'ƒ',
        'λ', 'Ω', 'µ', '†', '!', '£', '¢', '§',
        '¶', '•', '¡', '<', '>', 'A', 'E', 'I',
        'O', 'U','C', 'B', 'P', 'H', 'R', '&'] * 2
# Estado de la casilla
state = {'mark': None}
# Esconde las casillas
hide = [True] * 64
taps = 0 # numero de clicks al iniciar 

# Funcion que dibuja las casillas con los bordes
def square(x, y):
    "Dibuja un cuadrado blanco con borde negro en la posicion (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill() #inicia el relleno de color
    for count in range(4):
        forward(50)
        left(90)
    end_fill() #termina el relleno de color

# Funcion que convierte a coordenadas x & y las casillas con el indice seleccionado
def index(x, y):
    "Convierte las coordenadas (x, y) a un indice de casilla."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Funcion que convierte en casillas las coordenadas
def xy(count):
    "Convierte un numero de casilla a coordenadas (x, y)."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Funcion que marca cuando una casilla se ha seleccionado
def tap(x, y):
    "Actualiza la marca y oculta las casillas segun el click."
    global taps # variable taps
    taps += 1 # empieza a contar taps
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    print (f"Taps: {taps}.") # imprime la cantidad de taps

    if hide == [False] * 64:
        print("¡Has ganado!")
        

# Funcion que centra el texto en las casillas
def center_text(x, y, text):
    "Centra el texto en el cuadrado."
    up()
    goto(x + 25, y + 10)
    down()
    write(text, align = "center", font = ('Arial', 30, 'normal'))

# Funcion que dibuja la imagen si las casillas coinciden
def draw():
    "Dibuja la imagen y las casillas."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Recorre la lista y verificando si estan ocultas o no
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    # Se muestra el valor de la carta en la posicion seleccionada
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        center_text(x, y, tiles[mark])
    
    # Indicar que ya se han destapado todas los cuadros
    if hide == [False] * 64:
        goto(0,0)
        color('white')
        write("¡Has ganado!", align="center", font=('Arial', 30, 'bold'))
    
    update()
    ontimer(draw, 100)

shuffle(tiles) # Mezclar los simbolos en las casillas
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
