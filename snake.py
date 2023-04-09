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
    pink = ((255,100,180))
    purple = ((240,0,255))
    rust = ((210,150,75))
    forest_green = ((0,50,0))
    highlighter = ((255,255,100))
    marroon = ((115,0,0))
    coffee_brown =((200,190,140))
    blue_green = ((0,255,170))
    dark_gray = ((50,50,50))
    navy_blue = ((0,0,100))
    colours = [white, yellow, red, green, blue, pink, purple]

class parameter(): 
    dis_width = 600
    dis_height = 400

class snake():
    snake_block = 10
    snake_speed = 15
    snake_colour = colour.pink
    snake_length = 1
    snake_List = []  

class food():
    foodx = 0
    foody = 0
    colour_food = colour.green
    two = False
    one = True

class record():
    maxim = [0, 0, 0, 0, 0]

class level():
    k = [0.20, 0.25, 0.30, 0.35, 0.40]
    fod = [20, 10, 10, 0, 0]
    i = 0

class game_param():
    x1 = parameter.dis_width / 2
    y1 = parameter.dis_height / 2
    display_colour =  colour.black
    x1_change = 0
    y1_change = 0
    times = snake.snake_speed * snake.snake_length * level.k[level.i]

def table_record(value):
    record.maxim.append(value)
    record.maxim.sort(reverse = True)
    del record.maxim[-1]

def print_table():
    value = font_style.render("Your Score: " + str(record.maxim[0]) + ', ' + str(record.maxim[1]) + ', ' + str(record.maxim[2]) + ', ' + str(record.maxim[3]) + ', ' + str(record.maxim[4]), True, colour.red)
    dis.blit(value, [parameter.dis_width / 6 + 80, parameter.dis_height / 3 + 40])

dis = pygame.display.set_mode((parameter.dis_width, parameter.dis_height))
clock = pygame.time.Clock()
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, colour.marroon)
    dis.blit(value, [0, 0])
 
def our_snake():
    for x in snake.snake_List:
        pygame.draw.rect(dis, snake.snake_colour, [x[0], x[1], snake.snake_block, snake.snake_block])
  
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [parameter.dis_width / 6, parameter.dis_height / 3])

def food_generator():
    food.colour_food = random.choice(colour.colours)
    food.foodx = round(random.randrange(level.fod[level.i], parameter.dis_width - snake.snake_block - level.fod[level.i]) / 10.0) * 10.0
    food.foody = round(random.randrange(level.fod[level.i] + 55, parameter.dis_height - snake.snake_block - level.fod[level.i]) / 10.0) * 10.0

def loose():
    global game_close
    global game_first
    global game_over
    flag = True
    while game_close == True:
            dis.fill(colour.dark_gray)
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

def bonus():
    scale = snake.snake_length - 1
    if ((scale >= 10) and (scale < 12)) or ((scale % 10 == 0) and (scale > 0)):
        game_param.display_colour = colour.forest_green
    elif (scale >= 10) and (scale % 15 == 0):
        game_param.display_colour = colour.navy_blue
    else:
        game_param.display_colour = colour.black
    
    if (scale % 7 == 0) and (scale > 0):
        game_param.times = 5
    else:
        game_param.times = snake.snake_speed * snake.snake_length * level.k[level.i]

    if (scale % 5 == 0) and (scale > 0):
        food.two = True

def g_time():
    game_param.times = snake.snake_speed * snake.snake_length * level.k[level.i]

def start_game_parameter():
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
    snake.snake_length = 1
    food_generator()

def check_eat():
    if game_param.x1 == food.foodx and game_param.y1 == food.foody:
        food_generator()
        snake.snake_length += 1

def gameLoop():
    global game_close
    global game_first
    global game_over
    snake.snake_List = []
    start_game_parameter()
    choose_level()
    colour_of_snake()

    while not game_over:
        loose()
        move()
        bonus()

        game_param.x1 += game_param.x1_change
        game_param.y1 += game_param.y1_change
        snake_Head = []
        snake_Head.append(game_param.x1)
        snake_Head.append(game_param.y1)
        snake.snake_List.append(snake_Head)

        dis.fill(game_param.display_colour)
        for i in range(parameter.dis_width):
            pygame.draw.rect(dis, colour.red, [i, 50, 2, 2])

        pygame.draw.rect(dis, food.colour_food, [food.foodx, food.foody, snake.snake_block, snake.snake_block])
        if len(snake.snake_List) > snake.snake_length:
            del snake.snake_List[0]
        if game_param.x1 >= parameter.dis_width or game_param.x1 < 0 or game_param.y1 >= parameter.dis_height or game_param.y1 < 60:
            game_close = True
        for x in snake.snake_List[:-1]:
            if x == snake_Head:
                game_close = True 

 
        our_snake()
        Your_score(snake.snake_length - 1)
 
        pygame.display.update()

        check_eat()

        clock.tick(game_param.times)
 
    pygame.quit()
    quit()
 
gameLoop()