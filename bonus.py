import constant
from snake1 import snake
from table import record
from food import food
from level import level
from game_parameter import game_param

def bonus():
    scale = snake.snake_length - 1
    if ((scale >= 5) and (scale < 7)) or ((scale % 5 == 0) and (scale % 10 != 0)):
        game_param.display_colour = constant.colour.forest_green
    elif (scale >= 10) and (scale % 10 == 0):
        game_param.display_colour = constant.colour.navy_blue
    else:
        game_param.display_colour = constant.colour.black
    
    if (scale % 7 == 0) and (scale > 0):
        game_param.times = 5
    else:
        game_param.times = snake.snake_speed * snake.snake_length * level.k[level.i]

    if (scale % 5 == 0) and (scale > 0):
        food.two = True