import pygame

from Game import Game
from Player import Player
from Invaders import Invaders
import config as c


class SpaceInvaders(Game):
    def __init__(self):
        Game.__init__(self, 'Space Invaders', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        self.invaders = None
        self.player = None
        self.create_objects()

    def create_player(self):
        player = Player((c.screen_width - c.player_width) // 2,
                        c.screen_height - c.player_height * 2,
                        c.player_image,
                        c.player_width,
                        c.player_height)
        self.keydown_handlers[pygame.K_LEFT].append(player.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(player.handle)
        self.keyup_handlers[pygame.K_LEFT].append(player.handle)
        self.keyup_handlers[pygame.K_RIGHT].append(player.handle)
        self.player = player
        self.objects.append(self.player)

    def create_invaders(self):
        invaders = Invaders()
        self.invaders = invaders
        self.objects.append(self.invaders)

    def create_objects(self):
        self.create_player()
        self.create_invaders()

