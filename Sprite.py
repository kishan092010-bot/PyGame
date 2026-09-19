import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENTS = pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT+2

BLUE = pygame.Color("blue")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect