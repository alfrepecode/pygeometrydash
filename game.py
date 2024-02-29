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
        from camera import Camera
        self.blocks = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.map = self.read_file(map_path)
        self.map_width = len(self.map[0])*TILE_SIZE
        self.map_height = len(self.map)*TILE_SIZE
        self.camera = Camera(self.map_width, self.map_height)
        self.game_over = False
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

    def horizontal_movement(self):
        player = self.player.sprite
        player.pos.x += player.direction.x
        player.hit_rect.x = player.pos.x
        for block in self.blocks:
            if block.rect.colliderect(player.hit_rect):
                self.game_over = True
                player.hit_rect.right = block.rect.left
                player.pos.x = player.hit_rect.x
                
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
            self.player.sprite.kill()

    def update(self):
        player = self.player.sprite
        if player:
            self.horizontal_movement()
            self.vertical_movement()
            self.camera.update(self.player.sprite.rect)
            self.check_game_over()
        self.player.update()

    def draw(self, surface):
        player = self.player.sprite
        for block in self.blocks:
            surface.blit(block.image, self.camera.apply(block.rect))
        if player:
            surface.blit(player.image, self.camera.apply(player.rect))

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
        if game.game_over:
            game = Game('map.txt')
        screen.fill('lightblue')
        game.update()
        game.draw(screen)
        # draw_grid(screen)
        clock.tick(FPS)
        pygame.display.update()