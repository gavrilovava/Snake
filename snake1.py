from constant import colour
import pygame
from screen import parameter

class snake():
    snake_block = 10
    snake_speed = 15
    snake_colour = colour.pink
    snake_length = 1
    snake_List = []  

    def our_snake():
        for x in snake.snake_List:
            pygame.draw.rect(parameter.dis, snake.snake_colour, [x[0], x[1], snake.snake_block, snake.snake_block])
    