import pygame
import constant

pygame.init()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

class parameter(): 
    dis_width = 600
    dis_height = 400
    dis = pygame.display.set_mode((dis_width, dis_height))
    clock = pygame.time.Clock()

    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, constant.colour.marroon)
        parameter.dis.blit(value, [0, 0])
    
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        parameter.dis.blit(mesg, [parameter.dis_width / 6, parameter.dis_height / 3])
        






