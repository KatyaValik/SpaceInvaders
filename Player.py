import pygame
from Game_object import GameObject


class Player(GameObject):
    def __init__(self, x, y, image, width, height):
        GameObject.__init__(self, x, y, width, height, [1, 0])
        self.surf = pygame.image.load(image)
        self.rect = self.surf.get_rect()
        self.moving_left = False
        self.moving_right = False

    def draw(self, surface):
        # surface.blit(self.surf, self.rect)
        pygame.draw.rect(surface, (0, 255, 0), self.bounds)

    def handle(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        else:
            self.moving_right = not self.moving_right

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

