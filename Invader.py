import pygame
import config as c
from Game_object import GameObject


class Invader(GameObject):
    def __init__(self, x, y, image, width, height, left=False, right=False):
        GameObject.__init__(self, x, y, width, height, [1, 0])
        # self.surf = pygame.image.load(image)
        # self.rect = self.surf.get_rect()
        self.the_left = left
        self.the_right = right
        self.moving_to_left = False
        self.killed = False

    def draw(self, surface):
        # surface.blit(self.surf, self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.bounds)

    def update(self):
        if self.moving_to_left:
            self.move(-self.speed[0], 0)
        else:
            self.move(self.speed[0], 0)


