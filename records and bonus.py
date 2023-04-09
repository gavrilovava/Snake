def bonus():
    scale = snake.snake_length - 1
    if ((scale >= 5) and (scale < 7)) or ((scale % 5 == 0) and (scale % 10 != 0)):
        game_param.display_colour = colour.forest_green
    elif (scale >= 10) and (scale % 10 == 0):
        game_param.display_colour = colour.navy_blue
    else:
        game_param.display_colour = colour.black
    

    if (scale % 7 == 0) and (scale > 0):
        game_param.times = 5
    else:
        game_param.times = snake.snake_speed * snake.snake_length * level.k[level.i]