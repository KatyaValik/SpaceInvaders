import pygame
from Game import Game
from Player import Player
from Invaders import Invaders
from Shelter import Shelter
import config as c


class SpaceInvaders(Game):
    def __init__(self):
        Game.__init__(self, 'Space Invaders',
                      c.screen_width,
                      c.screen_height,
                      c.background_image,
                      c.frame_rate)
        self.invaders = None
        self.player = None
        self.shelters = None
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
        self.create_shelters()

    def create_shelters(self):
        self.shelters = []
        shelter_count = c.screen_width // (c.shelter_space + c.shelter_width)
        shelter_y = self.player.centery - 30
        for i in range(0, shelter_count):
            shelter = Shelter(c.shelter_space // 2 + i * (c.shelter_space + c.shelter_width),
                              shelter_y,
                              c.shelter_image,
                              c.shelter_width,
                              c.shelter_height)
            self.shelters.append(shelter)
            self.objects.append(shelter)

    def kill_invaders(self):
        for row in self.invaders.invaders:
            for invader in row:
                for bullet in self.player.bullets:
                    if pygame.Rect.colliderect(invader.bounds, bullet.bounds):
                        row.remove(invader)
                        self.player.bullets.remove(bullet)

    def kill_player(self):
        for space_bullet in self.invaders.space_bullets:
            if pygame.Rect.colliderect(space_bullet.bounds, self.player.bounds):
                self.player.killed = True

    def kill_space_bullet(self):
        for bullet in self.invaders.space_bullets:
            for shelter in self.shelters:
                if pygame.Rect.colliderect(bullet.bounds, shelter.bounds):
                    self.invaders.space_bullets.remove(bullet)
                    if shelter.damage_counter == c.shelter_damage_max:
                        self.shelters.remove(shelter)
                        self.objects.remove(shelter)
                    else:
                        shelter.damage_counter = shelter.damage_counter + 1

    def kill_bullet(self):
        for bullet in self.player.bullets:
            for shelter in self.shelters:
                if pygame.Rect.colliderect(bullet.bounds, shelter.bounds):
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
        if self.invaders.killed:
            self.win()
        if self.invaders.lost or self.player.killed:
            self.lose()
        if not self.game_is_running:
            return
        self.kill_invaders()
        self.kill_player()
        self.kill_space_bullet()
        self.kill_bullet()
        super().update()


