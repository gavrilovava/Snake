from src.screen import parameter
from src.constant import colour, const
from src.snake1 import snake
import random
from src.level import level

class food():
    foodx = 0
    foody = 0
    colour_food = colour.green
    two = False
    one = True

    def food_generator():
        food.colour_food = random.choice(colour.colours)
        food.foodx = round(random.randrange(level.fod[level.i], parameter.dis_width - snake.snake_block - level.fod[level.i]) / const.okr) * const.okr
        food.foody = round(random.randrange(level.fod[level.i] + const.delta_y_line, parameter.dis_height - snake.snake_block - level.fod[level.i]) / const.okr) * const.okr
