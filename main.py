
import pygame
from pygame.constants import K_SPACE
from pygame.display import update
from bird import Bird

pygame.init()
screen = pygame.display.set_mode((800, 800))
run = True
bg = pygame.image.load("background.png")

bird = Bird(50, 250)
brid_y = 200
bird_velocity = 0 
bird_acceleration = 0.25
jump_strength = -5 

fps = 32
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    bird_velocity += bird_acceleration
    bird.y += bird_velocity
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
               bird_velocity = jump_strength
        if 
    screen.blit(bird.image, bird.rect)
    screen.blit(bg, (0, 0))
    pygame.display.update()
pygame.quit()