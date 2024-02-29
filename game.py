import pygame, sys, os
from utils import *
from player import Player

pygame.init()
WIDTH, HEIGHT = 918, 476
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
TILE_SIZE = 34

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, img_path):
        super().__init__()
        self.image = load_image(img_path, (width, height))
        self.rect = self.image.get_rect(topleft = pos)

class Game:
    def __init__(self, map_path):
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.map = self.read_file(map_path)
        self.load_map()

    def read_file(self, path):
        file = ''
        with open(path, 'r') as f:
            file = f.read().splitlines()
        return file
    
    def load_map(self):
        for y, row in enumerate(self.map):
            for x, char in enumerate(row):
                if char == 'B':
                    self.blocks.add(Block((x*TILE_SIZE, y*TILE_SIZE), TILE_SIZE, TILE_SIZE, os.path.join('imgs', 'block.png')))
                elif char == 'P':
                    self.player.add(Player((x*TILE_SIZE, y*TILE_SIZE), TILE_SIZE, TILE_SIZE, os.path.join('imgs', 'player.png')))
                    
    def draw(self, surface):
        self.blocks.draw(surface)
        self.player.draw(surface)

def draw_grid(surface):
    for y in range(TILE_SIZE, WIDTH, TILE_SIZE):
        pygame.draw.line(surface, 'red', (y, 0), (y, HEIGHT))

    for x in range(TILE_SIZE, HEIGHT, TILE_SIZE):
        pygame.draw.line(surface, 'blue', (0, x), (WIDTH, x))

game = Game('map.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('lightblue')
    game.draw(screen)
    # draw_grid(screen)
    clock.tick(FPS)
    pygame.display.update()