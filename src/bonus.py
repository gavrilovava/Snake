import src.constant as constant
from src.snake1 import snake
from src.table import record
from src.food import food
from src.level import level
from src.game_parameter import game_param

def bonus():
    scale = snake.snake_length - 1
    if ((scale >= constant.const.screen_colour[0]) and (scale < constant.const.screen_colour[1])) or ((scale % constant.const.screen_colour[0] == 0) and (scale % constant.const.screen_colour[2] != 0)):
        game_param.display_colour = constant.colour.forest_green
    elif (scale >= constant.const.screen_colour[2]) and (scale % constant.const.screen_colour[2] == 0):
        game_param.display_colour = constant.colour.navy_blue
    else:
        game_param.display_colour = constant.colour.black
    
    if (scale % constant.const.screen_colour[1] == 0) and (scale > 0):
        game_param.times = constant.const.screen_colour[0]
    else:
        game_param.times = snake.snake_speed * snake.snake_length * level.k[level.i]