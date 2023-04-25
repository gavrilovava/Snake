from src.constant import colour
import src.constant as constant
import pygame
from src.screen import parameter

class snake():
    snake_block = constant.const.snake_block
    snake_speed = constant.const.snake_speed
    snake_colour = colour.pink
    snake_length = 1
    snake_List = []  

    def our_snake():
        for x in snake.snake_List:
            pygame.draw.rect(parameter.dis, snake.snake_colour, [x[0], x[1], snake.snake_block, snake.snake_block])
    