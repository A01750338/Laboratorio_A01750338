"""
   Actividad 4. Juego del Tiro Parabólico
   Modificaciones:
    - Hacer más rápida la velocidad del movimiento para el proyectil y los balones
    - Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se reposicionen 
"""

from random import randrange
from turtle import *
from freegames import vector

# Inicializacion de la posicion y velocidad de la pelota
ball = vector(-200, -200)
speed = vector(0, 0)
targets = [] # Lista vacia para los objetivos

# Funcion para responder al toque
def tap(x, y):
    "Responde a un toque en la pantalla."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

# Funciona para ver si el punto xy esta dentro de la pantalla
def inside(xy):
    "Devuelve true si el punto xy esta dentro de la pantalla. Si la bola esta fuera de la pantalla, ajusta su posicion y la velocidad de acuerdo al toque"
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Funcion para dibujar bola y objetivos
def draw():
    "Dibuja la bola y los objetivos."
    clear()

    # Dibujar los objetivos
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
  
    # Dibujar si la bola esta dentro de la pantalla
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

# Funcion para mover los objetos
def move():
    "Mover la bola y los objetivos."
    
    # Agregar aleatoriamente nuevos objetivos
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Mover los objetivos hacia la izquierda
    for target in targets:
        target.x -= 0.5

    # Si la pelota está dentro de la pantalla, mover la bola
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    # Duplicar la lista de objetivos
    dupe = targets.copy()
    targets.clear()

    # Eliminar los objetivos que chocaron con la bola
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Verificar si algun objetivo esta fuera de la pantalla
    for target in targets:
        if not inside(target):
            pass # para que el juego sea infinito

    ontimer(move, 25) # Aumentar velocidad del juego

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move() # Iniciar el movimiento de la bola y los objetivos
done()
