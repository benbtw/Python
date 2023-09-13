from player import *
from pytmx import *
from pytmx import load_pygame

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(100, 100)
player = Player(100, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    player.update(dt)
    player.draw(screen)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()