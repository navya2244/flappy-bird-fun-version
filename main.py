
import pygame
from pygame.display import update
from bird import Bird

pygame.init()
screen = pygame.display.set_mode((800, 800))
run = True
bg = pygame.image.load("background.png")
frame = 0
bird = pygame.image.load("bluebird-midflap.png")
bird_x = 50
bird_y = 250
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
   


    screen.blit(bg, (0, 0))
    screen.blit(bird,(bird_x,bird_y))
    pygame.display.update()
pygame.quit()