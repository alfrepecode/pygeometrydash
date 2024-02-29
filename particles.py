import pygame, sys
from random import uniform

pygame.init()
WIDTH, HEIGHT = 918, 476
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
vec = pygame.math.Vector2

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, vel, size, color, gravity):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = pos)
        self.pos = vec(pos)
        self.vel = vec(vel)
        self.gravity = gravity
        self.opacity = 255
    
    def update(self):
        self.pos += self.vel
        self.vel.y += self.gravity
        self.rect.topleft = self.pos
        self.image.set_alpha(self.opacity)
        self.opacity -= 12
        if self.opacity <= 0:
            self.kill()

if __name__ == '__main__':
    particles = pygame.sprite.Group()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('lightblue')
        particles.add(Particle(pygame.mouse.get_pos(), (uniform(-4.5, -0.5), uniform(-0.8, -0.5)), 7, 'white', 0.1))
        particles.update()
        particles.draw(screen)
        clock.tick(FPS)
        pygame.display.update()