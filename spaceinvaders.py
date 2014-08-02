#!/usr/bin/env python
import pygame
from pygame.locals import *
from spaceinvaders_sprites import *
import sys

# game init
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.key.set_repeat(400, 30)
clock = pygame.time.Clock()

# groups & sprites
all_sprites_group = pygame.sprite.Group()

# add sprites to their group
player = Player()
all_sprites_group.add(player)

for i in xrange(8):
    for j in xrange(8):
        enemy = Enemy((i+1)*(ENEMY_WIDTH + 5), (j+1)*(ENEMY_HEIGHT + 5))
        all_sprites_group.add(enemy)

# game loop
while True:
    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move_left()
            elif event.key == K_RIGHT:
                player.move_right()
            elif event.key == K_SPACE:
                print 'firing'

    # render sprites
    window.fill((0, 0, 0))
    all_sprites_group.draw(window)

    # refresh screen
    all_sprites_group.update()
    clock.tick(60)
    pygame.display.flip()
