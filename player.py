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
        self.on_ground = True
        self.angle = 0
        self.copy_img = self.image.copy()
    
    def rotate_img(self):
        self.image = pygame.transform.rotate(self.copy_img, -self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)
    
    def rotate(self):
        self.angle %= 360
        if not self.on_ground:
            self.angle += 5
        else:
            if 0 <= self.angle <= 44:
                self.angle = 0
            elif 45 <= self.angle <= 134:
                self.angle = 90
            elif 135 <= self.angle <= 224:
                self.angle = 180
            elif 225 <= self.angle <= 314:
                self.angle = 270
            else:
                self.angle = 0
        self.rotate_img()
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.pos.y += self.direction.y
        self.rect.y = self.pos.y
    
    def update(self):
        self.rotate()
        self.direction.x = self.speed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.on_ground:
            self.direction.y = self.initial_jump
            self.on_ground = False