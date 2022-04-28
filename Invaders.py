from Invader import Invader
from Game_object import GameObject
import config as c


class Invaders(GameObject):
    def __init__(self):
        self.invaders = None
        self.create_invaders()
        self.last_row = None

    def create_invaders(self):
        w = c.screen_width
        invaders_count_x = (w // (c.invader_width + c.invader_offset_x)) // 2
        invaders_count_y = c.invaders_start_count
        self.last_row = invaders_count_y
        invaders = []
        for row in range(invaders_count_y):
            invaders_row = []
            for col in range(invaders_count_x):
                left = False
                right = False
                if col == 0:
                    left = True
                elif col == invaders_count_x - 1:
                    right = True
                invader = Invader(col * (c.invader_width + c.invader_offset_x),
                                  row * (c.invader_height + c.invader_offset_y),
                                  c.invader_image,
                                  c.invader_width,
                                  c.invader_height,
                                  left, right)
                print('x = ', row * (c.invader_width + c.invader_offset_x))
                print('y = ', col * (c.invader_height + c.invader_offset_y))
                invaders_row.append(invader)
            invaders.append(invaders_row)
        self.invaders = invaders

    def change_direction(self):
        for invaders_row in self.invaders:
            for invader in invaders_row:
                invader.moving_to_left = not invader.moving_to_left
                invader.move(0, c.invader_down_offset)

    def update(self):
        for invader in self.invaders[0]:
            if invader.the_left and invader.moving_to_left and invader.left - invader.speed[0] < 0:
                self.change_direction()
                break
            elif invader.the_right and not invader.moving_to_left and invader.right + invader.speed[0] > c.screen_width:
                self.change_direction()
                break
        for invaders_row in self.invaders:
            for invader in invaders_row:
                invader.update()

    def draw(self, surface):
        for invaders_row in self.invaders:
            for invader in invaders_row:
                invader.draw(surface)

