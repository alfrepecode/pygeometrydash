import pygame, sys
from game import WIDTH, HEIGHT, TILE_SIZE

pygame.init()
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0,0, self.width, self.height)
    
    def apply(self, target_rect):
        return pygame.Rect(target_rect.x + self.rect.x, target_rect.y + self.rect.y, target_rect.width, target_rect.height)
    
    def update(self, target_rect):
        x = -target_rect.centerx + WIDTH//2
        y = -target_rect.centery + HEIGHT//2
        self.rect = pygame.Rect(x, y, self.width, self.height)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(center = pos)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 6
        if keys[pygame.K_a]:
            self.rect.x -= 6
        if keys[pygame.K_s]:
            self.rect.y += 6
        if keys[pygame.K_w]:
            self.rect.y -= 6

if __name__ == '__main__':        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('lightblue')
        clock.tick(FPS)
        pygame.display.update()