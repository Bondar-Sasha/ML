import pygame
from Platform.Platform import Platform
from Player import Player

class BluePlatform(Platform):
    def __init__(self,player: Player):
        super().__init__(player)
        self.image = pygame.transform.scale(pygame.image.load("./src/assets/blue.png"), (self.width, self.height)).convert_alpha(),
        self.direction = 1


    def moveX(self,screen: pygame.Surface):
        if self.x >= 500:
            self.direction = -1    
        elif self.x <= 0:
            self.direction = 1
            
        self.x += 25 * self.direction
        screen.blit(self.image, (self.x, self.y))