import pygame
from Game_object import GameObject


class Bullet(GameObject):
    def __init__(self, x, y, image, width, height):
        GameObject.__init__(self, x, y, width, height, [0, 3])
        # self.surf = pygame.image.load(image)
        # self.rect = self.surf.get_rect()

    def draw(self, surface):
        """ Отрисовывает пулю """
        # surface.blit(self.surf, self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.bounds)

    def update(self):
        """ Обновляет координаты пули """
        self.move(0, -self.speed[1])
