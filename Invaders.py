from Invader import Invader
from Game_object import GameObject
import config as c


class Invaders(GameObject):
    def __init__(self):
        self.invaders = None
        self.create_invaders()
        self.last_row = None
        self.killed = False
        self.lost = False

        self.x_left = c.screen_width
        self.x_right = 0

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
        if len(self.invaders) == 0:
            self.killed = True
            return
        else:
            for row in self.invaders:
                if len(row) == 0:
                    self.invaders.remove(row)
            if len(self.invaders) == 0:
                self.killed = True
                return
            else:
                x_left = c.screen_width
                x_right = 0

                # x_left = self.x_left
                # for row1 in self.invaders:
                #     if row1[0].left < x_left:
                #         x_left = row1[0].left
                # self.x_left = x_left
                #
                # x_right = self.x_right
                # for row2 in self.invaders:
                #     if row2[len(row2) - 1].right > x_right:
                #         x_right = row2[len(row2) - 1].right
                # self.x_right = x_right
                # print(x_right)

                for row1 in self.invaders:
                    for inv in row1:
                        if inv.left < x_left:
                            x_left = inv.left
                self.x_left = x_left

                for row2 in self.invaders:
                    for inv in row2:
                        if inv.right > x_right:
                            x_right = inv.right
                self.x_right = x_right

                # if self.invaders[len(self.invaders) - 1][0].bottom >= c.invaders_down_border:
                #     self.lost = True

        for invader in self.invaders[0]:
            if invader.left == self.x_left and invader.moving_to_left and invader.left - invader.speed[0] < 0:
                self.change_direction()
                break
            elif invader.right == self.x_right and not invader.moving_to_left and invader.right + invader.speed[0] > c.screen_width:
                self.change_direction()
                break
        for invaders_row in self.invaders:
            for invader in invaders_row:
                invader.update()

    def draw(self, surface):
        for invaders_row in self.invaders:
            for invader in invaders_row:
                invader.draw(surface)

