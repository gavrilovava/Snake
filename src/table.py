from src.screen import parameter
import pygame
from src.constant import colour, const

class record():
    maxim = [0, 0, 0, 0, 0]

    def table_record(value):
        record.maxim.append(value)
        record.maxim.sort(reverse = True)
        del record.maxim[-1]

    def print_table():
        font_style = pygame.font.SysFont("bahnschrift", const.letter_size_1)
        score_font = pygame.font.SysFont("comicsansms", const.letter_size_2)
        value = font_style.render("Your record: " + str(record.maxim[0]) + ', ' + str(record.maxim[1]) + ', ' + str(record.maxim[2]) + ', ' + str(record.maxim[3]) + ', ' + str(record.maxim[4]), True, colour.red)
        parameter.dis.blit(value, [parameter.dis_width / const.letter_x + const.letter_delta_x, parameter.dis_height / const.letter_y + const.letter_delta_y])
