from screen import parameter
import pygame
from constant import colour

class record():
    maxim = [0, 0, 0, 0, 0]

    def table_record(value):
        record.maxim.append(value)
        record.maxim.sort(reverse = True)
        del record.maxim[-1]

    def print_table():
        font_style = pygame.font.SysFont("bahnschrift", 25)
        score_font = pygame.font.SysFont("comicsansms", 35)
        value = font_style.render("Your Score: " + str(record.maxim[0]) + ', ' + str(record.maxim[1]) + ', ' + str(record.maxim[2]) + ', ' + str(record.maxim[3]) + ', ' + str(record.maxim[4]), True, colour.red)
        parameter.dis.blit(value, [parameter.dis_width / 6 + 80, parameter.dis_height / 3 + 40])