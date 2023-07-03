import pygame
import random

class Meteoro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("imagenes\meteoro\Meteor_10.png"),(60,60))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 12

        if self.rect.y > 970:
            self.rect.y = -70
            self.rect.x = random.randrange(1200)

class MeteoroDos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("imagenes\meteoro\Meteor_10.png"),(60,60))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 8

        if self.rect.y > 970:
            self.rect.y = -70
            self.rect.x = random.randrange(1200)

class MeteoroTres(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("imagenes\meteoro\Meteor_10.png"),(60,60))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 8

        if self.rect.y > 970:
            self.rect.y = -70
            self.rect.x = random.randrange(1200)