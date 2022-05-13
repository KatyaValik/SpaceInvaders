import pygame
import sys
from collections import defaultdict


class Game:
    def __init__(self,
                 caption,
                 width,
                 height,
                 back_image_filename,
                 frame_rate):
        self.background_image = \
            pygame.image.load('C:/Users/Ekaterina/PycharmProjects/python_2sem/Space_Invaders/' + back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        pygame.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)

    def handle_events(self):
        """Функция проверяет условие закрытие окна и завершает программу
            Вызывает обработчики для всех событий, которые возникли в очередной итерации главного цикла игры"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)

    def update(self):
        """ Обновляет все объекты в игре """
        for o in self.objects:
            o.update()

    def draw(self):
        """ Отрисовывает все объекты в игре """
        for o in self.objects:
            o.draw(self.surface)

    def run(self):
        """ Главный цикл игры:
                вызывает функции для отлавливания событий, обновления и отрисовки объектов игры, обновдения экрана
                обновляет таймер игры
                """
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
