import pygame, sys

pygame.init()
WIDTH, HEIGHT = 918, 476
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Death(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((200, 200), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = pos)
        self.opacity = 255
        self.radius = 0
    
    def update(self):
        pygame.draw.circle(self.image, (142, 142, 142, self.opacity),(self.image.get_width()//2, self.image.get_height()//2),self.radius)
        self.radius += 3
        self.opacity -= 6
        
if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('lightblue')
        clock.tick(FPS)
        pygame.display.update()