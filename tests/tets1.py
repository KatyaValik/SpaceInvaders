import unittest
from Space_invaders import SpaceInvaders
import pygame


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.space_invaders = SpaceInvaders()
        self.space_invaders.create_player()
        self.player = self.space_invaders.player

    def test_shoot(self):
        start_count = len(self.player.bullets)
        self.player.handle(pygame.K_SPACE)
        self.player.update()
        end_count = len(self.player.bullets)
        self.assertEqual(1, end_count - start_count)

    def test_moving_left(self):
        start_coord = self.player.left
        self.player.handle(pygame.K_LEFT)
        self.player.update()
        end_coord = self.player.left
        self.assertEqual(3, start_coord - end_coord)

    def test_moving_right(self):
        start_coord = self.player.left
        self.player.handle(pygame.K_RIGHT)
        self.player.update()
        end_coord = self.player.left
        self.assertEqual(3, end_coord - start_coord)

    def test_stops_at_the_right_wall(self):
        self.player.move(286, 0)
        self.player.handle(pygame.K_RIGHT)
        self.player.update()
        end_coord = self.player.right
        self.assertEqual(600, end_coord)

    def test_stops_at_the_left_wall(self):
        self.player.move(- self.player.left + 2, 0)
        self.player.handle(pygame.K_LEFT)
        self.player.update()
        end_coord = self.player.left
        self.assertEqual(0, end_coord)


if __name__ == "__main__":
    unittest.main()
