import pygame
from pygame.sprite import Sprite
import os

class Alien(Sprite):

    def __init__(self, settings, screen):
        super(Alien, self).__init__()

        mypath = os.path.dirname(os.path.realpath(__file__))
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load(os.path.join(mypath, 'alienship.png'))
        self.image = pygame.transform.scale(self.image, (50, 20))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        

    def blitThis(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Move the alien right or left
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True