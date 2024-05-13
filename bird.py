import pygame 

class Bird: 


  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
    self.delta = 2
    self.up = True
    self.down = False
  def move(self):
    if self.up:
      self.y -= self.delta
    if self.down:
      self.y += self.delta
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
