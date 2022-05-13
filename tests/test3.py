import unittest
from Space_invaders import SpaceInvaders
from Space_bullet import SpaceBullet
import config as c


class TestShelters(unittest.TestCase):
    def setUp(self):
        self.space_invaders = SpaceInvaders()
        self.space_invaders.create_shelters()

    def test_shelter_damage(self):
        x = self.space_invaders.shelters[0].centerx
        y = self.space_invaders.shelters[0].centery
        space_bullet = SpaceBullet(x, y, "images//background.jpg", 5, 10)
        self.space_invaders.invaders.space_bullets.append(space_bullet)
        start_count = len(self.space_invaders.invaders.space_bullets)
        start_damage = self.space_invaders.shelters[0].damage_counter
        self.space_invaders.kill_space_bullet()
        self.assertEqual(1, start_count - len(self.space_invaders.invaders.space_bullets))
        self.assertEqual(1, self.space_invaders.shelters[0].damage_counter - start_damage)

    def test_delete_shelter(self):
        x = self.space_invaders.shelters[0].centerx
        y = self.space_invaders.shelters[0].centery
        space_bullet = SpaceBullet(x, y, "images//background.jpg", 5, 10)
        self.space_invaders.invaders.space_bullets.append(space_bullet)
        start_count = len(self.space_invaders.shelters)
        self.space_invaders.shelters[0].damage_counter = c.shelter_damage_max
        self.space_invaders.kill_space_bullet()
        self.assertEqual(1, start_count - len(self.space_invaders.shelters))


if __name__ == "__main__":
    unittest.main()

