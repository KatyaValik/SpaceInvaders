from Game_object import GameObject
import config as c
import pygame


class Shelter(GameObject):
    def __init__(self, x, y, image, width, height):
        GameObject.__init__(self, x, y, width, height)
        self.damage_counter = 0

    def draw(self, surface):
        """ Отрисовывает укрытие """
        pygame.draw.rect(surface, c.shelter_colours[self.damage_counter], self.bounds)

