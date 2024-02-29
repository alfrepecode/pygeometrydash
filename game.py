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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('lightblue')
    blocks.draw(screen)
    clock.tick(FPS)
    pygame.display.update()