import pygame
import time
import random
 
pygame.init()

game_over = False
game_close = False
game_first = True

class colour(): 
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    colours = [white, yellow, red, green, blue]

class parameter(): 
    dis_width = 600
    dis_height = 400

class snake():
    snake_block = 10
    snake_speed = 15
    snake_colour = colour.white
    snake_length = 1   

class food():
    foodx = 0
    foody = 0
    colour_food = colour.green


class game_param():
    x1 = parameter.dis_width / 2
    y1 = parameter.dis_height / 2
    x1_change = 0
    y1_change = 0

class record():
    maxim = [0, 0, 0, 0, 0]


def table_record(value):
    record.maxim.append(value)
    record.maxim.sort(reverse = True)
    del record.maxim[-1]

def print_table():
    value = font_style.render("Your Score: " + str(record.maxim[0]) + ', ' + str(record.maxim[1]) + ', ' + str(record.maxim[2]) + ', ' + str(record.maxim[3]) + ', ' + str(record.maxim[4]), True, colour.green)
    dis.blit(value, [parameter.dis_width / 6 + 80, parameter.dis_height / 3 + 40])

dis = pygame.display.set_mode((parameter.dis_width, parameter.dis_height))
clock = pygame.time.Clock()
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, colour.yellow)
    dis.blit(value, [0, 0])
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snake.snake_colour, [x[0], x[1], snake_block, snake_block])
  
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [parameter.dis_width / 6, parameter.dis_height / 3])

def food_generator():
    food.colour_food = random.choice(colour.colours)
    food.foodx = round(random.randrange(0, parameter.dis_width - snake.snake_block) / 10.0) * 10.0
    food.foody = round(random.randrange(0, parameter.dis_height - snake.snake_block) / 10.0) * 10.0

def loose():
    global game_close
    global game_first
    global game_over
    flag = True
    while game_close == True:
            dis.fill(colour.blue)
            message("You Lost! Press C-Play Again or Q-Quit", colour.red)
            Your_score(snake.snake_length - 1)
            if flag:
                table_record(snake.snake_length - 1)
                flag = False
            print_table()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
def move():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
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

def gameLoop():
    global game_close
    global game_first
    global game_over
    game_param.x1 = parameter.dis_width / 2
    game_param.y1 = parameter.dis_height / 2
    game_param.x1_change = 0
    game_param.y1_change = 0
    game_over = False
    game_close = False
    game_first = True
    snake_List = []
    snake.snake_length = 1
    food_generator()
    #colour_of_snake()

    while not game_over:
        loose()
        move()
        
        if game_param.x1 >= parameter.dis_width or game_param.x1 < 0 or game_param.y1 >= parameter.dis_height or game_param.y1 < 0:
            game_close = True

        game_param.x1 += game_param.x1_change
        game_param.y1 += game_param.y1_change
        dis.fill(colour.black)
        pygame.draw.rect(dis, food.colour_food, [food.foodx, food.foody, snake.snake_block, snake.snake_block])
        snake_Head = []
        snake_Head.append(game_param.x1)
        snake_Head.append(game_param.y1)
        snake_List.append(snake_Head)
        if len(snake_List) > snake.snake_length:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake.snake_block, snake_List)
        Your_score(snake.snake_length - 1)
 
        pygame.display.update()

        if game_param.x1 == food.foodx and game_param.y1 == food.foody:
            food_generator()
            snake.snake_length += 1
 
        clock.tick(snake.snake_speed * snake.snake_length * 0.25)
 
    pygame.quit()
    quit()
 
gameLoop()