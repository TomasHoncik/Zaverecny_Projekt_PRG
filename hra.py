import pygame
from pygame import *
import pygame.display

pygame.init()

SCREEN_WIDTH = 563
SCREEN_HEIGHT = 630

# pes

TEXT_COLOUR = (255,255,255)
font = pygame.font.SysFont("arialblack",30)



screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def draw_text(text,font,text_colour, x, y):
    img = font.render(text, True, text_colour)
    screen.blit(img,(x,y))

run = True
while run:
#  229, 252, 245 183, 247, 227
    screen.fill((160, 244, 219))

    draw_text("Vítej v mojí hře!",font,TEXT_COLOUR, 143,50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()