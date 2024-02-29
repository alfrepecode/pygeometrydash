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

class Game:
    def __init__(self, map_path):
        self.blocks = pygame.sprite.Group()
        self.map = self.read_file(map_path)

    def read_file(self, path):
        file = ''
        with open(path, 'r') as f:
            file = f.read().splitlines()
        return file
    
    def load_map(self):
        for row in self.map:
            for char in row:
                if char == 'B':
                    self.blocks.add(Block((0,0), 34, 34, os.path.join('imgs', 'block.png')))
                    
    def draw(self, surface):
        self.blocks.draw(surface)

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
    clock.tick(FPS)
    pygame.display.update()