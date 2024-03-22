# ![Logo del freegames](https://pypi.org/static/images/logo-small.2a411bc6.svg) Proyecto - Desarrollo de videojuegos en Python
Este proyecto tiene como objetivo desarrollar pequeños juegos utilizando Python y la librería Turtle. A través de este proyecto, aprenderemos a utilizar herramientas computacionales útiles, como:
- Uso de terminales para controlar tu computadora
- Instalación de software desde la línea de comando
- Edición, compilación y ejecución de programas desde la línea de comando
- Uso de herramientas para control de versiones de código

## 📋 Pre-requisitos 
- **Python 3.X** <br>
  - **Windows**:\
     Descargar python 3.X desde https://www.python.org/downloads/

  - **macOS**:\
    Se puede instalar utilizando [Homebrew](https://brew.sh/) ejecutando el siguiente comando en la terminal:
    ```
    brew install python3
    ```
    
  - **Linux**:\
    Se puede instalar a través del gestor de paquetes de la distribución:
    ```
    sudo apt-get update
    sudo apt-get install python3
    ```

  📝La instalación de Python 3 generlamente incluye pip automáticamente.
<br></br>
- **pip instalado**\
  pip es una herramienta que facilita la instalación de paquetes y bibliotecas de Python.  
  Para verificar si pip está instalado, ejecutar el siguiente comando en la terminal:
  ```
  python -m pip --version
  ```
  Si está instalado, se observará la información sobre la versión instalada.
<br></br>
- **Libreria 'freegames'**\
  Una vez ya instalado el pip, se puede instalar las bibliotecas de Python necesarias.
  
  **Freegames**: Esta biblioteca proporciona un conjunto de juegos simples para aprender a programar en Python.\
  Se puede instalar utilizando el siguiente comando en la terminal:
  ```
  pip install freegames
  ```
  Para consultar su contenido:
  ```
  python3 -m freegames list
  ```
  Para jugar cualquiera de los juegos desde la terminal:
  ```
  python3 -m freegames.snake
  ```
  Para modificar y correr juego:
  ```
  python3 -m freegames copy snake
  python3 snake.py
  ```


## 💻 Modificaciones realizadas 
### Juego Pintando
- Agregar un color nuevo
- Dibujar un circulo, rectangulo y triangulo

### Juego de la Víbora
- Mover comida al azar un paso a la vez
- Cambiar de colores al azar la comida y la víbora cada vez que que se corra el juego

### Juego del Packman
- Hacer que los fantasmar sean mas listos
- Cambiar el tablero
- Hacer que los fantasmas vayan mas rapido

### Juego del Tiro Parabólico
- Hacer más rápida la velocidad del movimiento para el proyectil y los balones
- Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se reposicionen 

### Juego de Memoria
- Contar y desplegar el numero de taps
- Detectar cuando todos los cuadros se han destapado
- Centrar el dígito en el cuadro
- Utilizar algo diferente a los dígitos para resolver el juego

## 🖋️Autores
- Andrea Elizabeth Román Varela
- Min Che Kim
