from Platform.Platform import Platform
from Player import Player
import pygame

class GreenPlatform(Platform):
    def __init__(self, player: Player):
        super().__init__(player)
        self.images = pygame.transform.scale(pygame.image.load("./src/assets/green.png"), (self.width, self.height)).convert_alpha(),
