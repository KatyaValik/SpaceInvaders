import pygame
from Game import Game
from Player import Player
from Invaders import Invaders
from Shelter import Shelter
from Text_object import TextObject
from Saucer import Saucer
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
        self.score = 0
        self.level_number = 0
        self.shelters = None
        self.saucer = None
        self.score_label = None
        self.lives_label = None
        self.levels_label = None
        self.create_objects()
        self.game_is_running = True
        self.saucer_timer = time.time()

    def create_player(self):
        """ СОздает игрока """
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
        self.keyup_handlers[pygame.K_a].append(player.handle)
        self.keydown_handlers[pygame.K_a].append(player.handle)
        self.keyup_handlers[pygame.K_d].append(player.handle)
        self.keydown_handlers[pygame.K_d].append(player.handle)
        self.player = player
        self.objects.append(self.player)

    def create_invaders(self):
        """ создает захватчиков """
        invaders = Invaders(eval(c.levels[self.level_number]).invaders_rows,
                            eval(c.levels[self.level_number]).invaders_columns,
                            eval(c.levels[self.level_number]).hardy_invaders_count)
        self.invaders = invaders
        self.objects.append(self.invaders)

    def create_objects(self):
        """ Вызывает функции для создания всех объектов в игре """
        self.create_player()
        self.create_invaders()
        self.create_shelters()
        self.create_labels()

    def create_shelters(self):
        """ Создает укрытия """
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

    def create_saucer(self):
        """ Создает тарелку по прошествии заданного времени  """
        if time.time() - self.saucer_timer >= c.saucer_pause:
            saucer = Saucer(c.screen_width, c.saucer_offset, c.saucer_image, c.saucer_width, c.saucer_height)
            self.objects.append(saucer)
            self.saucer = saucer
            self.saucer_timer = time.time()

    def create_labels(self):
        """ Создает текстовые поля для демонстрации прогресса в игре:
            количества жизней игрока, номер текущего уровня и количство набранных очков """
        self.score_label = TextObject(c.score_offset,
                                      c.status_offset_y,
                                      lambda: f'SCORE: {self.score}',
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
        """ Проверяет попадание пули игрока в захватчиков и удаляет захватчика из игры"""
        for row in self.invaders.invaders:
            for invader in row:
                for bullet in self.player.bullets:
                    if pygame.Rect.colliderect(invader.bounds, bullet.bounds):
                        if invader.type == 0:
                            row.remove(invader)
                            self.player.bullets.remove(bullet)
                            self.score = self.score + 1
                        else:
                            invader.type = 0
                            self.player.bullets.remove(bullet)

    def kill_player(self):
        """ Проверяет попадание пули захватчика в игора и уменьшает количество жизней игрока """
        for space_bullet in self.invaders.space_bullets:
            if pygame.Rect.colliderect(space_bullet.bounds, self.player.bounds):
                self.invaders.space_bullets.remove(space_bullet)
                self.lives = self.lives - 1
                print(self.lives)
                if self.lives == 0:
                    self.player.killed = True

    def kill_space_bullet(self):
        """" Проверяет попадание пули захватчика в укрытие и увеличивает сетчик разрушения укрытия """
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
        """ Проверяет попадание пули игрока в укрытие и удаляет эту пулю """
        for bullet in self.player.bullets:
            for shelter in self.shelters:
                if pygame.Rect.colliderect(bullet.bounds, shelter.bounds):
                    self.player.bullets.remove(bullet)

    def kill_saucer(self):
        """ Проверяет попала ли пуля игрока в тарелку, увеличивает счет и удаляет тарелку и пулю """
        if self.saucer is not None:
            for bullet in self.player.bullets:
                if self.saucer is not None:
                    if pygame.Rect.colliderect(bullet.bounds, self.saucer.bounds):
                        self.player.bullets.remove(bullet)
                        self.objects.remove(self.saucer)
                        self.saucer = None
                        self.score = self.score + c.saucer_score

    def delete_saucer(self):
        """ Удаляет тарелку, когда она улетает за пределы окна """
        if self.saucer is not None and self.saucer.right <= 0:
            self.objects.remove(self.saucer)
            self.saucer = None

    def show_message(self, text, color=(255, 255, 255), font_name='Arial', font_size=20, centralized=False):
        """ Функция для отображения текста на экране """
        message = TextObject(c.screen_width // 2, c.screen_height // 2, lambda: text, color, font_name, font_size)
        self.draw()
        message.draw(self.surface, centralized)
        pygame.display.update()
        time.sleep(c.message_duration)

    def win(self):
        """ Оповещает игрока о конце игры в случае выигрыша """
        self.show_message('YOU WON!', centralized=True)
        self.game_is_running = False
        self.game_over = True

    def lose(self):
        """ Оповещает игрока о конце игры в случае проигрыша """
        self.show_message('GAME OVER!', centralized=True)
        self.game_is_running = False
        self.game_over = True

    def new_level(self):
        """ Оповещает игрока о переходе на новый уровень,
            вызывает функцию для создания объектов следующего уровня"""
        self.show_message(f'LEVEL: {self.level_number + 1}', centralized=True)
        self.objects = []
        self.create_objects()
        self.invaders.score = self.score

    def update(self):
        """Проверяет условия перехода на слующий уровень или окончания игры,
            вызывает фунции удаления требующихся игровых объектов"""
        if self.invaders.killed and self.level_number == c.levels_count:
            self.win()
        if self.invaders.lost or self.player.killed:
            self.lose()
        if self.invaders.killed and self.level_number < c.levels_count:
            self.level_number = self.level_number + 1
            self.new_level()
        if not self.game_is_running:
            return
        self.create_saucer()
        self.kill_invaders()
        self.kill_player()
        self.kill_space_bullet()
        self.kill_bullet()
        self.delete_saucer()
        self.kill_saucer()
        super().update()
