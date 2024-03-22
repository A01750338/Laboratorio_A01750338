"""
   Actividad 1. Juego Pintando
   Modificaciones:
    - Agregar un color nuevo
    - Dibujar un circulo, rectangulo y triangulo
"""

from turtle import *
from freegames import vector

# Funcion que dibuja una linea 
def line(start, end):
    "Dibujar linea de inicio a fin"
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Funcion que dibuja un cuadrado
def square(start, end):
    "Dibujar cuadrado de inicio a fin"
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Funcion que dibuja un circulo
def circle(start, end):
    "Dibujar circulo de inicio a fin."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(360):
        forward(1)
        left(1)

    end_fill()

# Funcion que dibuja un rectangulo
def rectangle(start, end):
    "Dibujar rectangulo de inicio a fin."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    
    end_fill()

# Funcion que dibuja un triangulo
def triangle(start, end):
    "Dibujar triangulo de inicio a fin."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    for count in range(2):
        forward(end.x - start.x)
        left(70)
    
    end_fill()

# Funciona para detectar punto de inicio y final al hacer clic 
def tap(x, y):
    "Guardar punto de inicio o dibujar la forma"
    start = state['start']

    if start is None: # Si no hay punto de inicio
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Almacena un valor en el estado asociado a una clave."
    state[key] = value

# Estado inicial al correr el juego
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
# Teclas para cambiar color
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('magenta'), 'M') # <- Nuevo color
# Teclas para cambiar de forma
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
