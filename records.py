class record():
    maxim = [0, 0, 0, 0, 0]


def table_record(value):
    record.maxim.append(value)
    record.maxim.sort(reverse = True)
    del record.maxim[-1]

def print_table():
    value = score_font.render("Your Score: " + str(record.maxim), True, colour.yellow)
    dis.blit(value, [parameter.dis_width / 6 + 10, parameter.dis_height / 3 + 10])
for i in range(20):
    table_record(i)
    print(record.maxim)



    def colour_of_snake():
    print('Write w to choose white colour of snake, y - yellow, r - red, g -green, b -blue')
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