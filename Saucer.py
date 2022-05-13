import config as c
import pygame
from Game_object import GameObject


class Saucer(GameObject):
    def __init__(self, x, y, image, width, height):
        GameObject.__init__(self, x, y, width, height, [-2, 0])
        # self.surf = pygame.image.load(image)
        # self.rect = self.surf.get_rect()
        self.killed = False

    def draw(self, surface):
        """ Отрисовывает тарелку """
        # surface.blit(self.surf, self.rect)
        pygame.draw.rect(surface, (254, 0, 236), self.bounds)


