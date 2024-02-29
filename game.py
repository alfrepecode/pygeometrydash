import pygame, sys, os
from utils import *
from player import Player
from death_ani import Death
from particles import Particle
from random import uniform
vec = pygame.math.Vector2

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

class Spike(Block):
    def __init__(self, pos, width, height, img_path, rotate=False):
        super().__init__(pos, width, height, img_path)        
        if rotate:
            self.image = pygame.transform.rotate(self.image, 180)

class Game:
    def __init__(self, map_path):
        from camera import Camera
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.map = self.read_file(map_path)
        self.map_width = len(self.map[0])*TILE_SIZE
        self.map_height = len(self.map)*TILE_SIZE
        self.camera = Camera(self.map_width, self.map_height)
        self.game_over = False
        self.status = ''
        self.level_end = 0
        self.death_ani = pygame.sprite.GroupSingle()
        self.particles = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
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
                elif char == 'S':
                    self.spikes.add(Spike((x*TILE_SIZE, y*TILE_SIZE), TILE_SIZE, TILE_SIZE, os.path.join('imgs', 'spike.png')))
                elif char == 'R':
                    self.spikes.add(Spike((x*TILE_SIZE, y*TILE_SIZE), TILE_SIZE, TILE_SIZE, os.path.join('imgs', 'spike.png'), True))
                elif char == 'W':
                    self.level_end = x*TILE_SIZE

    def update_status(self):
        if self.player.sprite.pos.x >= self.level_end:
            self.status = 'Level completed'

    def horizontal_movement(self):
        player = self.player.sprite
        player.pos.x += player.direction.x
        player.hit_rect.x = player.pos.x
        for block in self.blocks:
            if block.rect.colliderect(player.hit_rect):
                self.game_over = True
                player.hit_rect.right = block.rect.left
                player.pos.x = player.hit_rect.x

        if pygame.sprite.spritecollide(player, self.spikes, False, pygame.sprite.collide_mask):                
            self.game_over = True
            
    def vertical_movement(self):
        player = self.player.sprite
        player.apply_gravity()
        for block in self.blocks:
            if block.rect.colliderect(player.hit_rect):
                if player.direction.y < 0:
                    self.game_over = True
                    player.hit_rect.top = block.rect.bottom
                    player.pos.y = player.hit_rect.y
                    player.direction.y = 0
                if player.direction.y > 0:
                    player.on_ground = True
                    player.hit_rect.bottom = block.rect.top
                    player.pos.y = player.hit_rect.y
                    player.direction.y = 0
        
        if player.on_ground and player.direction.y < 0 or player.direction.y > 0:
            player.on_ground = False

    def check_game_over(self):
        if self.game_over:
            self.death_ani.add(Death(self.camera.apply(self.player.sprite.rect).center))
            self.player.sprite.kill()

    def update(self):
        player = self.player.sprite
        if player:
            if player.on_ground:
                self.particles.add(Particle(self.camera.apply(self.player.sprite.rect).bottomleft+vec(3,-6), (uniform(-4.5, -0.5), uniform(-0.8, -0.5)), 7, 'white', 0.1))
            self.horizontal_movement()
            self.vertical_movement()
            self.camera.update(self.player.sprite.rect)
            self.update_status()
            self.check_game_over()
        self.player.update()
        self.death_ani.update()
        self.particles.update()

    def draw(self, surface):
        player = self.player.sprite
        self.particles.draw(surface)
        for block in self.blocks:
            surface.blit(block.image, self.camera.apply(block.rect))
        for spike in self.spikes:
            surface.blit(spike.image, self.camera.apply(spike.rect))
        if player:
            surface.blit(player.image, self.camera.apply(player.rect))
        self.death_ani.draw(surface)
        draw_center_text(surface, self.status, (WIDTH//2, HEIGHT//2), 20, 'black')

def draw_grid(surface):
    for y in range(TILE_SIZE, WIDTH, TILE_SIZE):
        pygame.draw.line(surface, 'red', (y, 0), (y, HEIGHT))

    for x in range(TILE_SIZE, HEIGHT, TILE_SIZE):
        pygame.draw.line(surface, 'blue', (0, x), (WIDTH, x))

if __name__ == '__main__':
    game = Game('map.txt')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if game.game_over and game.death_ani.sprite is None:
            game = Game('map.txt')
        screen.fill('lightblue')
        game.update()
        game.draw(screen)
        # draw_grid(screen)
        clock.tick(FPS)
        pygame.display.update()