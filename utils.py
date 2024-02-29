import pygame, os

def load_image(path, size=None):
    img = pygame.image.load(path)
    if size:
        img = pygame.transform.scale(img, size)
    return img

def draw_center_text(surface, text, pos, font_size, color):
    font = pygame.font.Font(os.path.join("fonts","Vera.ttf"), font_size)
    image = font.render(text, True, color)
    rect = image.get_rect(center = pos)
    surface.blit(image, rect)
