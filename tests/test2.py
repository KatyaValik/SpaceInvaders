import unittest
from Space_invaders import SpaceInvaders
from Bullet import Bullet


class TestInvaders(unittest.TestCase):
    def setUp(self):
        self.space_invaders = SpaceInvaders()
        self.space_invaders.create_invaders()

    def test_kill_invader(self):
        self.space_invaders.invaders.invaders[0][0].type = 0
        x = self.space_invaders.invaders.invaders[0][0].centerx
        y = self.space_invaders.invaders.invaders[0][0].centery
        start_count = len(self.space_invaders.invaders.invaders)
        bullet = Bullet(x, y, "images//background.jpg", 5, 10)
        self.space_invaders.create_player()
        self.space_invaders.player.bullets.append(bullet)
        self.space_invaders.kill_invaders()
        self.assertEqual(1, start_count - len(self.space_invaders.invaders.invaders[0]))

    def test_kill_hardly_invader(self):
        self.space_invaders.invaders.invaders[0][0].type = 1
        x = self.space_invaders.invaders.invaders[0][0].centerx
        y = self.space_invaders.invaders.invaders[0][0].centery
        start_count = len(self.space_invaders.invaders.invaders)
        bullet = Bullet(x, y, "images//background.jpg", 5, 10)
        self.space_invaders.create_player()
        self.space_invaders.player.bullets.append(bullet)
        self.space_invaders.kill_invaders()
        self.assertEqual(0, start_count - len(self.space_invaders.invaders.invaders[0]))
        self.assertEqual(0, self.space_invaders.invaders.invaders[0][0].type)


if __name__ == "__main__":
    unittest.main()
