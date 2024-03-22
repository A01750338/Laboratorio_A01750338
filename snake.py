"""
   Actividad 2. Juego de la Víbora
   Modificaciones:
    - Mover comida al azar un paso a la vez
    - Cambiar de colores al azar la comida y la víbora
      cada vez que que se corra el juego
"""

from turtle import *
from random import randrange
from freegames import square, vector
import random

# Inicializar variables
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Indicar colores
color = ['green', 'blue', 'black', 'purple', 'orange']
c1 = random.randint(0,4)
c2 = random.randint(0,4)

snake_c = color[c1]
food_c = color[c2]

if snake_c == food_c:
    snake_c = color[2]
    food_c = color[0]

# Funcion para cambiar de direccion
def change(x, y):
    "Cambia la direccion de la serpiente."
    aim.x = x
    aim.y = y

# Funcion para validar el tablero
def inside(head):
    "Detecta si la cabeza de ls serpiente esta dentro de los limites del tablero."
    return -200 < head.x < 190 and -200 < head.y < 190

# Funcion para mover la comida
def move_food():
    "Mueve la comida un paso al azar sin salirse de la ventana."
    food.x += randrange(-1, 2) * 10
    food.y += randrange(-1, 2) * 10
    if not inside(food):
        if food.x < -190:
            food.x = -180
        elif food.x > 180:
            food.x = 170
        if food.y < -190:
            food.y = -180
        elif food.y > 180:
            food.y = 170
    ontimer(move_food, 1500)

# Funcion para mover al serpiente
def move():
    "Mueve la serpiente un segmento hacia adelante y actualiza el estado del juego."
    head = snake[-1].copy()
    head.move(aim)

    # Verifica si la cabeza esta dentro del tablero o si ha chocado consigo misma
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    
    # Verificar si la serpiente comio la comida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
    else:
        snake.pop(0)

    clear()

    # Dibujar la serpiente y la comida 
    for body in snake:
        square(body.x, body.y, 9, snake_c)

    square(food.x, food.y, 9, food_c)
    update()
    ontimer(move, 100)

# Configuracion inicial de la pantalla
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Teclas para mover al serpiente
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Iniciar el movimiento de la serpiente
move()
move_food()
done()
