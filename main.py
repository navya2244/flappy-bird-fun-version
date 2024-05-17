
import pygame
from pygame.constants import K_SPACE
from pygame.display import update
from bird import Bird

pygame.init()
screen = pygame.display.set_mode((800, 800))
run = True
bg = pygame.image.load("background.png")
bird_image = pygame.image.load("bluebird-midflap.png")
bird = Bird(50, 250)
bird_y = 200
bird_velocity = 0 
bird_acceleration = 0.25
jump_strength = -5 

fps = 32
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.KEYDOWN:
            Bird.move(bird, K_SPACE)
    #     if event.type == pygame.KEYDOWN and event.key == K_SPACE:
    #         bird_velocity = jump_strength
    # bird_velocity += bird_acceleration
    # bird.y += int(bird_velocity)
    
    screen.blit(bg, (0, 0))
    screen.blit(bird.image, (50, 250))    

    pygame.display.update()
pygame.quit()