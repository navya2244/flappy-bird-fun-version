import pygame

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("bluebird-midflap.png")
        self.image_size = self.image.get_size()  # Define image_size before rescaling
        self.rescale_image()  # Call rescale_image after defining image_size
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.delta = 5
        self.is_jumping = False
        self.is_falling = False
        self.vel_y = 0
        self.jump_strength = -15
        self.gravity = 1

    def rescale_image(self):
        scale_size = (int(self.image_size[0] * 0.7), int(self.image_size[1] * 0.7))
        self.image = pygame.transform.scale(self.image, scale_size)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jumping and self.rect.bottom >= 600:
            self.is_jumping = True
            self.vel_y = self.jump_strength

        self.vel_y += self.gravity
        self.rect.y += self.vel_y

        if self.rect.bottom >= 600:  # Assuming the ground level is at y = 600
            self.rect.bottom = 600
            self.is_jumping = False
            self.vel_y = 0