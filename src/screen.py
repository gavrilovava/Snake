import pygame
import src.constant as constant

pygame.init()

font_style = pygame.font.SysFont("bahnschrift", constant.const.letter_size_1)
score_font = pygame.font.SysFont("comicsansms", constant.const.letter_size_2)

class parameter(): 
    dis_width = constant.const.width
    dis_height = constant.const.height
    dis = pygame.display.set_mode((dis_width, dis_height))
    clock = pygame.time.Clock()

    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, constant.colour.marroon)
        parameter.dis.blit(value, [0, 0])
    
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        parameter.dis.blit(mesg, [parameter.dis_width / constant.const.letter_x, parameter.dis_height / constant.const.letter_y])
        






