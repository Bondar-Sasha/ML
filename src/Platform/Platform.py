import random
from Player import Player

class Platform():
    def __init__(self, player: Player):
        self.player = player
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 700)
        self.width = 100 
        self.height = 25 

    def setOnPlatform(self,onPlatform: bool) -> None:
        self.player.onPlatform = onPlatform
        
    def update(self) -> None:
        if (self.x < self.player.x < self.x + self.width) and (self.y < self.player.y < self.y + self.height):
            self.setOnPlatform(True)
            return
        self.setOnPlatform(False)
    
    