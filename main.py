
import pygame
from pygame.constants import K_0, K_SPACE
from pygame.display import update
from bird import Bird

pygame.init()
screen = pygame.display.set_mode((800, 800))
run = True
bg = pygame.image.load("background.png")
bird_image = pygame.image.load("bluebird-midflap.png")
bird_y = 200
bird_x = 50
bird = Bird(bird_x, bird_y)
bird_velocity = 0 
bird_acceleration = 0.25
jump_strength = -5 
y = bird_y
fps = 32
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.KEYUP:
                bird.move()
    
    screen.blit(bg, (0, 0))
    screen.blit(bird.image, bird.rect)    

    pygame.display.update()
pygame.quit()