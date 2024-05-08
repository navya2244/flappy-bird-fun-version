
import pygame
from pygame.display import update
from bird import Bird

pygame.init()
screen = pygame.display.set_mode((270, 500))
run = True
bg = pygame.image.load("background-day.png")

bird = Bird(100, 100)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False


    bird = pygame.image.load("bluebird-midflap.png")
    screen.blit(bg, (0, 0))
    screen.blit(bird,(100,100))
    pygame.display.update()
pygame.quit()