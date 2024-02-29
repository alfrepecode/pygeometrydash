import pygame, sys, os
from utils import *

pygame.init()
WIDTH, HEIGHT = 918, 476
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, img_path):
        super().__init__()
        self.image = load_image(img_path, (width, height))
        self.rect = self.image.get_rect(topleft = pos)

blocks = pygame.sprite.Group()
blocks.add(Block((0,0), 34, 34, os.path.join('imgs', 'block.png')))
blocks.add(Block((34,0), 34, 34, os.path.join('imgs', 'block.png')))

def draw_grid(surface):
    for y in range(34, WIDTH, 34):
        pygame.draw.line(surface, 'red', (y, 0), (y, HEIGHT))

    for x in range(34, HEIGHT, 34):
        pygame.draw.line(surface, 'blue', (0, x), (WIDTH, x))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('lightblue')
    draw_grid(screen)
    blocks.draw(screen)
    clock.tick(FPS)
    pygame.display.update()