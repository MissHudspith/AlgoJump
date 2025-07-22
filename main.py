# Imports
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 480, 640
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Algo Jump")
clock = pygame.time.Clock()

# Colours
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Player values
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
GRAVITY = 0.5
JUMP_STRENGTH = -10 # Negative to jump up as going against gravity

# Platform values
PLATFORM_WIDTH = 80
PLATFORM_HEIGHT = 15
PLATFORM_DISTANCE = 90

# Font
font = pygame.font.SysFont("consolas", 24)

# Class Definitions

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 150)
        self.vel_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        # Move left or right with relevant key press
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Apply gravity using constant defined earlier
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Wrap around screen 
        if self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = WIDTH

    def jump(self):
        self.vel_y = JUMP_STRENGTH


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y): # x and y values passed in when creating each platform
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


platforms = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Generate starting platforms
for i in range(7):
    x = random.randint(0, WIDTH - PLATFORM_WIDTH)
    y = i * PLATFORM_DISTANCE
    p = Platform(x, y)
    platforms.add(p)
    all_sprites.add(p)


# MAIN GAME LOOP
running = True

while running:
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player
    player.update()

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
    

pygame.quit()

