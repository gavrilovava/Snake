from screen import parameter
from constant import colour
from snake1 import snake

class level():
    k = [0.20, 0.25, 0.30, 0.35, 0.40]
    fod = [20, 10, 10, 0, 0]
    i = 0

    def choose_level():
        print('Choose level from 1 to 5:')
        levele = int(input())
        level.i = levele - 1

    def colour_of_snake():
        print('Write w to choose white colour of snake, y - yellow, r - red, g -green, b -blue, p - pink')
        bucova = input()
        if bucova == 'w':
            snake.snake_colour = colour.white
        elif bucova == 'y':
            snake.snake_colour = colour.yellow
        elif bucova == 'r':
            snake.snake_colour = colour.red
        elif bucova == 'g':
            snake.snake_colour = colour.green
        elif bucova == 'b':
            snake.snake_colour = colour.blue
        elif bucova == 'p':
            snake.snake_colour = colour.pink

def start_choise():
    level.choose_level()
    level.colour_of_snake()