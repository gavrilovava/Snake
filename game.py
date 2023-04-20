import pygame
import time
import random
from screen import parameter
from level import level, start_choise
from table import record
from food import food
from game_parameter import game_param
import constant
from snake1 import snake
import game
from bonus import bonus

pygame.init()
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
                        
def move():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            constant.game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_param.x1_change = -snake.snake_block
                game_param.y1_change = 0
            elif event.key == pygame.K_RIGHT:
                game_param.x1_change = snake.snake_block
                game_param.y1_change = 0
            elif event.key == pygame.K_UP:
                game_param.y1_change = -snake.snake_block
                game_param.x1_change = 0
            elif event.key == pygame.K_DOWN:
                game_param.y1_change = snake.snake_block
                game_param.x1_change = 0

def loose():
    flag = True
    while constant.game_close == True:
            parameter.dis.fill(constant.colour.dark_gray)
            parameter.message("You Lost! Press C-Play Again or Q-Quit", constant.colour.red)
            parameter.Your_score(snake.snake_length - 1)
            if flag:
                record.table_record(snake.snake_length - 1)
                flag = False
            record.print_table()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        constant.game_over = True
                        constant.game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

def gameLoop():
    snake.snake_List = []
    game_param.start_game_parameter()
    start_choise()

    while not constant.game_over:
        loose()
        game.move()
        bonus()

        game_param.x1 += game_param.x1_change
        game_param.y1 += game_param.y1_change
        snake_Head = []
        snake_Head.append(game_param.x1)
        snake_Head.append(game_param.y1)
        snake.snake_List.append(snake_Head)

        parameter.dis.fill(game_param.display_colour)
        for i in range(parameter.dis_width):
            pygame.draw.rect(parameter.dis, constant.colour.red, [i, 50, 2, 2])

        pygame.draw.rect(parameter.dis, food.colour_food, [food.foodx, food.foody, snake.snake_block, snake.snake_block])
        if len(snake.snake_List) > snake.snake_length:
            del snake.snake_List[0]
        if game_param.x1 >= parameter.dis_width or game_param.x1 < 0 or game_param.y1 >= parameter.dis_height or game_param.y1 < 60:
            constant.game_close = True
        for x in snake.snake_List[:-1]:
            if x == snake_Head:
                constant.game_close = True 

 
        snake.our_snake()
        parameter.Your_score(snake.snake_length - 1)
 
        pygame.display.update()

        game_param.check_eat()

        parameter.clock.tick(game_param.times)
 
    pygame.quit()
    quit()