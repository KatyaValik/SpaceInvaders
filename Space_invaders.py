import pygame
from Game import Game
from Player import Player
from Invaders import Invaders
from Shelter import Shelter
from Text_object import TextObject
import config as c
import level1
import level2
import level3
import time


class SpaceInvaders(Game):
    def __init__(self):
        Game.__init__(self, 'Space Invaders',
                      c.screen_width,
                      c.screen_height,
                      c.background_image,
                      c.frame_rate)
        self.invaders = None
        self.player = None
        self.lives = c.initial_lives
        self.level_number = 0
        self.shelters = None
        self.score_label = None
        self.lives_label = None
        self.levels_label = None
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
        eval(c.levels[self.level_number]).invaders_rows
        invaders = Invaders(eval(c.levels[self.level_number]).invaders_rows,
                            eval(c.levels[self.level_number]).invaders_columns)
        self.invaders = invaders
        self.objects.append(self.invaders)

    def create_objects(self):
        self.create_player()
        self.create_invaders()
        self.create_shelters()
        self.create_labels()

    def create_shelters(self):
        self.shelters = []
        shelter_count = eval(c.levels[self.level_number]).shelters_count
        for i in range(0, shelter_count):
            shelter = Shelter(eval(c.levels[self.level_number]).shelters_coordinates[i][0],
                              eval(c.levels[self.level_number]).shelters_coordinates[i][1],
                              c.shelter_image,
                              eval(c.levels[self.level_number]).shelters_coordinates[i][2],
                              c.shelter_height)
            self.shelters.append(shelter)
            self.objects.append(shelter)

    def create_labels(self):
        self.score_label = TextObject(c.score_offset,
                                      c.status_offset_y,
                                      lambda: f'SCORE: {self.invaders.score}',
                                      c.text_color,
                                      c.font_name,
                                      c.font_size)
        self.objects.append(self.score_label)
        self.lives_label = TextObject(c.lives_offset,
                                      c.status_offset_y,
                                      lambda: f'LIVES: {self.lives}',
                                      c.text_color,
                                      c.font_name,
                                      c.font_size)
        self.objects.append(self.lives_label)
        self.levels_label = TextObject(c.levels_offset,
                                       c.status_offset_y,
                                       lambda: f'LEVEL: {self.level_number + 1}',
                                       c.text_color,
                                       c.font_name,
                                       c.font_size)
        self.objects.append(self.levels_label)

    def kill_invaders(self):
        for row in self.invaders.invaders:
            for invader in row:
                for bullet in self.player.bullets:
                    if pygame.Rect.colliderect(invader.bounds, bullet.bounds):
                        row.remove(invader)
                        self.player.bullets.remove(bullet)
                        self.invaders.score = self.invaders.score + 1

    def kill_player(self):
        for space_bullet in self.invaders.space_bullets:
            if pygame.Rect.colliderect(space_bullet.bounds, self.player.bounds):
                self.invaders.space_bullets.remove(space_bullet)
                self.lives = self.lives - 1
                print(self.lives)
                if self.lives == 0:
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

    def show_message(self, text, color=(255, 255, 255), font_name='Arial', font_size=20, centralized=False):
        message = TextObject(c.screen_width // 2, c.screen_height // 2, lambda: text, color, font_name, font_size)
        self.draw()
        message.draw(self.surface, centralized)
        pygame.display.update()
        time.sleep(c.message_duration)

    def win(self):
        self.show_message('YOU WON!', centralized=True)
        self.game_is_running = False
        self.game_over = True

    def lose(self):
        self.show_message('GAME OVER!', centralized=True)
        self.game_is_running = False
        self.game_over = True

    def new_level(self):
        self.objects = []
        self.create_objects()

    def update(self):
        if self.invaders.killed and self.level_number == c.levels_count:
            self.win()
        if self.invaders.lost or self.player.killed:
            self.lose()
        if self.invaders.killed and self.level_number < c.levels_count:
            self.level_number = self.level_number + 1
            self.new_level()
        if not self.game_is_running:
            return
        self.kill_invaders()
        self.kill_player()
        self.kill_space_bullet()
        self.kill_bullet()
        super().update()
