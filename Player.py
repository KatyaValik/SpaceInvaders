import pygame
from Game_object import GameObject
from Bullet import Bullet
import config as c
import time


class Player(GameObject):
    def __init__(self, x, y, image, width, height):
        GameObject.__init__(self, x, y, width, height, [1, 0])
        # self.surf = pygame.image.load(image)
        # self.rect = self.surf.get_rect()
        self.moving_left = False
        self.moving_right = False
        self.bullets = []
        self.space_down = False
        self.timer_continuous = None
        self.timer_discontinuous = c.bullet_dist

    def draw(self, surface):
        # surface.blit(self.surf, self.rect)
        pygame.draw.rect(surface, (0, 255, 0), self.bounds)
        for bullet in self.bullets:
            bullet.draw(surface)

    def handle(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        elif key == pygame.K_RIGHT:
            self.moving_right = not self.moving_right
        elif key == pygame.K_SPACE and time.time() - self.timer_discontinuous > c.bullet_dist:
            self.space_down = True
            self.timer_continuous = time.time()
            bullet = Bullet(self.centerx, self.centery, c.bullet_image, c.bullet_width, c.bullet_height)
            self.bullets.append(bullet)

    def handle_up(self, key):
        if key == pygame.K_SPACE:
            self.timer_continuous = 0
            self.space_down = False
            self.timer_discontinuous = time.time()

    def update(self):
        if self.moving_left:
            if self.left - self.speed[0] < 0:
                self.move(0, 10)
                self.moving_left = False
            else:
                self.move(-self.speed[0], 0)
        elif self.moving_right:
            if self.right + self.speed[0] > 600:
                self.move(0, 10)
                self.moving_left = True
            else:
                self.move(self.speed[0], 0)
        if self.space_down:
            timer_diff = time.time() - self.timer_continuous
            if timer_diff >= c.bullet_pause:
                bullet = Bullet(self.centerx, self.centery, c.bullet_image, c.bullet_width, c.bullet_height)
                self.bullets.append(bullet)
                self.timer_continuous = time.time()
        for bullet in self.bullets:
            bullet.update()



