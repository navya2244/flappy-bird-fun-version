import pygame
from bird import Bird

pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

base = pygame.image.load("base.png")
bg = pygame.image.load("background.png")

bird = Bird(500, 500)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    bird.update()

    screen.blit(bg, (0, 0))
    screen.blit(bird.image, bird.rect)
 
    pygame.display.update()
    clock.tick(60)

pygame.quit()
