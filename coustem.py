import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Sprites with Custom Event")
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000) 
class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.color = (255, 0, 0)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def change_color(self):
        self.color = (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )
        self.image.fill(self.color)
sprite1 = MySprite(100, 150)
sprite2 = MySprite(400, 150)
sprites = pygame.sprite.Group()
sprites.add(sprite1)
sprites.add(sprite2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR:
            sprite1.change_color()
            sprite2.change_color()
    screen.fill((255,255,255))
    sprites.draw(screen)
    pygame.display.update()
pygame.quit()