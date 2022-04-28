import pygame

from Game import Game
from Player import Player
from Invaders import Invaders
from Bullet import Bullet
import config as c


class SpaceInvaders(Game):
    def __init__(self):
        Game.__init__(self, 'Space Invaders', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        self.invaders = None
        self.player = None
        self.create_objects()
        self.game_is_running = True

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
        self.keydown_handlers[pygame.K_SPACE].append(player.handle)
        self.keyup_handlers[pygame.K_SPACE].append(player.handle_up)
        self.player = player
        self.objects.append(self.player)

    def create_invaders(self):
        invaders = Invaders()
        self.invaders = invaders
        self.objects.append(self.invaders)

    def create_objects(self):
        self.create_player()
        self.create_invaders()

    def kill_invaders(self):
        for row in self.invaders.invaders:
            for invader in row:
                for bullet in self.player.bullets:
                    if pygame.Rect.colliderect(invader.bounds, bullet.bounds):
                        row.remove(invader)
                        # self.invaders.x_right = 0
                        # self.invaders.x_left = c.screen_width
                        self.player.bullets.remove(bullet)

    def win(self):
        print("YOU WON")
        self.game_is_running = False
        self.game_over = True

    def lose(self):
        print("YOU LOST")
        self.game_is_running = False
        self.game_over = True

    def update(self):
        if not self.game_is_running:
            return
        if self.invaders.killed:
            self.win()
        if self.invaders.lost:
            self.lose()
        self.kill_invaders()
        super().update()


