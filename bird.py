import pygame 

class Bird: 


  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.image = pygame.image.load("bluebird-midflap.png")
    self.rescale_image(self.image)
    self.image_size = self.image.get_size()
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1]) 
    self.delta = 3
    # jump code below
    self.is_jumping = True
    self.is_falling = False
    
  def rescale_image(self, image):

    self.image_size = self.image.get_size()
    scale_size = (self.image_size[0] * 0.7, self.image_size[1] * 0.7)
    self.image = pygame.transform.scale(self.image,scale_size)

  def move(self):
    keys = pygame.key.get_pressed()
    if keys == pygame.K_SPACE:
      self.y += self.delta
      self.x += self.delta
    else:
      self.y -= self.delta
      self.y = max(0, min(self.y, 600 - self.image_size[1]))
      self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

  
  def gravity(self):
    if self.is_jumping:
        self.y += 3.2
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
                        