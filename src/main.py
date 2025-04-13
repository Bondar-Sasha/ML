import pygame
import sys
import random
from Player import Player
from Platform.GreenPlatform import GreenPlatform
from Platform.BluePlatform import BluePlatform

# Инициализация Pygame
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()
FPS = 60

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Шрифт
font = pygame.font.SysFont('Arial', 30)

def main():
    # Создание игрока
    player = Player(screen)
    
    # Создание начальной платформы
    platforms = []
    start_platform = GreenPlatform(player)
    start_platform.x = SCREEN_WIDTH // 2 - start_platform.width // 2
    start_platform.y = SCREEN_HEIGHT - 100
    platforms.append(start_platform)
    
    # Игровые переменные
    score = 0
    scroll_y = 0
    game_over = False
    
    # Основной игровой цикл
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    # Перезапуск игры
                    return main()
        
        if not game_over:
            # Движение игрока по горизонтали
            player.moveX()
            
            # Автоматический прыжок при приземлении на платформу
            player.jump()
            
            # Проверка столкновений с платформами
            player.onPlatform = False
            for platform in platforms:
                platform.update()
                
                # Проверка столкновения игрока с платформой
                if (platform.x < player.x + 40 < platform.x + platform.width and
                    platform.y - 10 < player.y + 80 < platform.y + platform.height and
                    player.velocity_y > 0):
                    player.onPlatform = True
                    player.jump()
            
            # Применение гравитации
            if not player.onPlatform and not player.jumping:
                player.y += player.gravity
            
            # Прокрутка экрана вверх
            if player.y < SCREEN_HEIGHT // 3:
                scroll_y = SCREEN_HEIGHT // 3 - player.y
                player.y = SCREEN_HEIGHT // 3
                score += scroll_y
                
                # Перемещение платформ вниз
                for platform in platforms:
                    platform.y += scroll_y
                    
                    # Удаление платформ, ушедших за экран
                    if platform.y > SCREEN_HEIGHT:
                        platforms.remove(platform)
            
            # Генерация новых платформ
            while len(platforms) < 10:
                platform_type = random.choice([GreenPlatform, BluePlatform])
                new_platform = platform_type(player)
                new_platform.x = random.randint(0, SCREEN_WIDTH - new_platform.width)
                new_platform.y = random.randint(-100, -20)
                platforms.append(new_platform)
            
            # Проверка на проигрыш
            if player.y > SCREEN_HEIGHT - 50:
                game_over = True
        
        # Отрисовка
        screen.fill(BLACK)
        
        # Отрисовка платформ
        for platform in platforms:
            if isinstance(platform, GreenPlatform):
                screen.blit(platform.image, (platform.x, platform.y))
            elif isinstance(platform, BluePlatform):
                platform.moveX(screen)
        
        # Отрисовка игрока
        player.update()
        
        # Отрисовка счета
        score_text = font.render(f"Score: {int(score)}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # Отрисовка экрана проигрыша
        if game_over:
            game_over_text = font.render("Game Over! Press SPACE to restart", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()