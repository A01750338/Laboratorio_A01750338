from random import *
from turtle import *
from freegames import path

# se define la imagen que se utilizara
car = path('car.gif')
# simbolos que se mostraran
tiles = ['$', '?', '¿', '@', '+', '*', '%', 'ƒ',
        'λ', 'Ω', 'µ', '†', '!', '£', '¢', '§',
        '¶', '•', '¡', '<', '>', 'A', 'E', 'I',
        'O', 'U','C', 'B', 'P', 'H', 'R', '&'] * 2
# estado de la casilla
state = {'mark': None}
# esconde las casillas
hide = [True] * 64
taps = 0 #numero de clicks al iniciar 

# Funcion que dibuja las casillas con los bordes
def square(x, y):
    "Draw white square with black outline at (x, y)."
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
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Funcion que convierte en casillas las coordenadas
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Funcion que marca cuando una casilla se ha seleccionado
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global taps #variable taps
    taps += 1 #empieza a contar taps
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    print (f"Taps: {taps}.") #imprime la cantidad de taps

    if hide == [False] * 64:
        print("¡Has ganado!")

#Funcion que centra el texto en las casillas
def center_text(x, y, text):
    "Centers the text in the square"
    up()
    goto(x + 25, y + 10)
    down()
    write(text, align = "center", font = ('Arial', 30, 'normal'))

# Funcion que dibuja la imagen si las casillas coinciden
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

# se recorre la lista y verificando si estan ocultas o no
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
# Se muestra el valor de la carta en la posicion seleccionada
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        center_text(x, y, tiles[mark])

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
