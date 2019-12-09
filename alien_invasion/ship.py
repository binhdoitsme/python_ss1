import os
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, settings, screen):
        # attach this to a game screen
        mypath = os.path.dirname(os.path.realpath(__file__))
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load(os.path.join(mypath, 'ship.png'))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        super(Ship, self).__init__()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def blitThis(self):
        # screen.blit(object, position)
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and not self.touched_right_edge():
            self.rect.centerx += 1
        if self.moving_left and not self.touched_left_edge():
            self.rect.centerx -= 1

    def touched_right_edge(self) -> bool:
        return self.rect.centerx == (self.screen_rect.right - (self.rect.width / 2))

    def touched_left_edge(self) -> bool:
        return self.rect.centerx == (self.rect.width / 2)

    def center_ship(self):
        self.center = self.screen_rect.centerx