from screen import parameter
from constant import colour
from snake1 import snake
import random
from level import level

class food():
    foodx = 0
    foody = 0
    colour_food = colour.green
    two = False
    one = True

    def food_generator():
        food.colour_food = random.choice(colour.colours)
        food.foodx = round(random.randrange(level.fod[level.i], parameter.dis_width - snake.snake_block - level.fod[level.i]) / 10.0) * 10.0
        food.foody = round(random.randrange(level.fod[level.i] + 55, parameter.dis_height - snake.snake_block - level.fod[level.i]) / 10.0) * 10.0
