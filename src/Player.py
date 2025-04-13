import pygame
import time
import threading

class Player(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.screen = screen
        
        self.playerRight = pygame.transform.scale(
            pygame.image.load("./src/assets/right.png"), 
            (80, 80)
        ).convert_alpha()
        self.playerLeft = pygame.transform.scale(
            pygame.image.load("./src/assets/left.png"), 
            (80, 80)
        ).convert_alpha()
        
        self.x = 300
        self.y = 550
        self.facing = 1
        self.onPlatform = True  
        
        self.speed_x = 7
        
        self.jump_power = 15
        self.gravity = 3    
        self.jumping = False
    
    def jump(self) -> None:
        if self.onPlatform and not self.jumping:
            self.jumping = True
            jump_thread = threading.Thread(target=self.perform_jump)
            jump_thread.start()

    def perform_jump(self):
        for _ in range(3):
            self.y -= self.jump_power
            time.sleep(1)  
        self.jumping = False
            
    def moveX(self) -> None:
        if self.x > 545:
            self.x = -35
        elif self.x < -35:
            self.x = 545

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.facing = 1
            self.x += self.speed_x * self.facing
        elif keys[pygame.K_LEFT]:
            self.facing = -1
            self.x += self.speed_x * self.facing

    def update(self) -> None:
        if not self.jumping and not self.onPlatform:
            self.y += self.gravity
            
        if self.facing == 1:
            self.screen.blit(self.playerRight, (self.x, self.y))
        else:
            self.screen.blit(self.playerLeft, (self.x, self.y))
