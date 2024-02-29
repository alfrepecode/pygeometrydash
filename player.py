import pygame
from utils import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, img_path):
        super().__init__()
        self.image = load_image(img_path, (width, height))
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = vec(0,0)
        self.gravity = 0.8
        self.pos = vec(pos)
        self.initial_jump = -11
        self.speed = 5
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.pos.y += self.direction.y
        self.rect.y = self.pos.y
    
    def update(self):
        self.direction.x = self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.direction.y = self.initial_jump