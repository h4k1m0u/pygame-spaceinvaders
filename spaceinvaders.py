#!/usr/bin/env python
import pygame
from pygame.locals import *
from spaceinvaders_sprites import *
import sys

# game vars
score = 0
direction = 'right'
changing_direction = False

# game init
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders Game - Score: %s" % score)
pygame.key.set_repeat(300, 50)
clock = pygame.time.Clock()

# groups & sprites
sprites_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()

# add sprites to their group
player = Player()
sprites_group.add(player)

for i in xrange(8):
    for j in xrange(8):
        enemy = Enemy((i+1)*(ENEMY_WIDTH + 5), (j+1)*(ENEMY_HEIGHT + 5))
        sprites_group.add(enemy)
        enemies_group.add(enemy)

# sync enemies movement
pygame.time.set_timer(ENEMIES_EVENT, 500)

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
                bullet = Bullet(player.rect.x + PLAYER_WIDTH/2 - BULLET_WIDTH/2)
                bullets_group.add(bullet)
                sprites_group.add(bullet)
        elif event.type == ENEMIES_EVENT:
            enemies_group.update(direction)

            # detect collision between enemy & left|right screen
            if any(enemy.rect.x <= ENEMY_WIDTH or enemy.rect.x >= WINDOW_WIDTH-2*ENEMY_WIDTH for enemy in enemies_group):
                enemies_group.update('bottom')
                direction = 'left' if direction == 'right' else 'right'

    # detect collision between bullet & enemy
    if pygame.sprite.groupcollide(bullets_group, enemies_group, True, True):
        score += 1
        pygame.display.set_caption("Space Invaders Game - Score: %s" % score)

    # detect collision between enemy & bottom screen
    if any(enemy.rect.y > WINDOW_HEIGHT-2*PLAYER_HEIGHT for enemy in enemies_group):
        print 'Game Over'
        pygame.quit()
        sys.exit()

    # render sprites
    window.fill((0, 0, 0))
    sprites_group.draw(window)
    bullets_group.update()

    # refresh screen
    clock.tick(60)
    pygame.display.flip()
