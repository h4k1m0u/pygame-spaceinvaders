#!/usr/bin/env python
import pygame
from pygame.locals import USEREVENT

# constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

PLAYER_WIDTH = 32
PLAYER_HEIGHT = 23
PLAYER_SPEED = 20

ENEMY_WIDTH = 32
ENEMY_HEIGHT = 23
ENEMY_SPEED = 32

BULLET_WIDTH = 9
BULLET_HEIGHT = 9
BULLET_SPEED = 5

ENEMIES_EVENT = USEREVENT + 1


class Space_Invaders_Sprite(pygame.sprite.Sprite):
    """ Space Invaders sprites classes extend this classes

        Attributes:
            image_file (str): Sprite image filename.
    """
    def __init__(self, image_file):
        pygame.sprite.Sprite.__init__(self)

        # load image & rect
        self.image = pygame.image.load('images/' + image_file).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()


class Player(Space_Invaders_Sprite):
    """ Aircraf: Positionned at the bottom of the window,
        but can move horizontally.
    """
    def __init__(self):
        Space_Invaders_Sprite.__init__(self, 'player.png')
        self.rect.bottom = WINDOW_HEIGHT
        self.rect.left = (WINDOW_WIDTH - self.image.get_width()) / 2

    def move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-PLAYER_SPEED, 0)

    def move_right(self):
        if self.rect.right < WINDOW_WIDTH:
            self.rect.move_ip(PLAYER_SPEED, 0)


class Enemy(Space_Invaders_Sprite):
    """ Enemy: Positionned in (x, y), and moving horizontally and vertically.
    """
    def __init__(self, x, y):
        Space_Invaders_Sprite.__init__(self, 'enemy.png')
        self.rect.x, self.rect.y = x, y

    def update(self, direction='right'):
        if direction == 'left':
            self.rect.move_ip(-ENEMY_SPEED, 0)
        elif direction == 'right':
            self.rect.move_ip(ENEMY_SPEED, 0)
        elif direction == 'top':
            self.rect.move_ip(0, -ENEMY_SPEED)
        elif direction == 'bottom':
            self.rect.move_ip(0, ENEMY_SPEED)


class Bullet(Space_Invaders_Sprite):
    """ Bullet: shot vertically to the top.
    """
    def __init__(self, x):
        Space_Invaders_Sprite.__init__(self, 'bullet.png')
        self.rect.x, self.rect.y = x, WINDOW_HEIGHT - PLAYER_HEIGHT

    def update(self):
        self.rect.move_ip(0, -BULLET_SPEED)
