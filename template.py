import pygame, sys

pygame.init()
WIDTH, HEIGHT = 918, 476
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('lightblue')
    clock.tick(FPS)
    pygame.display.update()