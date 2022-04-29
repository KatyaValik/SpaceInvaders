from Game_object import GameObject
import pygame


class SpaceBullet(GameObject):
    def __init__(self, x, y, image, width, height):
        GameObject.__init__(self, x, y, width, height, [0, 1])

    def draw(self, surface):
        # surface.blit(self.surf, self.rect)
        pygame.draw.rect(surface, (255, 255, 0), self.bounds)

    def update(self):
        self.move(0, self.speed[1])
