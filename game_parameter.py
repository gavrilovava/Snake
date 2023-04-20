from screen import parameter
import constant
from snake1 import snake
from level import level
from food import food

class game_param():
    x1 = parameter.dis_width / 2
    y1 = parameter.dis_height / 2
    display_colour =  constant.colour.black
    x1_change = 0
    y1_change = 0
    times = snake.snake_speed * snake.snake_length * level.k[level.i]

    def start_game_parameter():
        game_param.x1 = parameter.dis_width / 2
        game_param.y1 = parameter.dis_height / 2
        game_param.x1_change = 0
        game_param.y1_change = 0
        constant.game_over = False
        constant.game_close = False
        constant.game_first = True
        snake.snake_length = 1
        food.food_generator()

    def check_eat():
        if game_param.x1 == food.foodx and game_param.y1 == food.foody:
            food.food_generator()
            snake.snake_length += 1

