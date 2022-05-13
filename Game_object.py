from pygame.rect import Rect


class GameObject:
    def __init__(self, x, y, w, h, speed=(0, 0)):
        self.bounds = Rect(x, y, w, h)
        self.speed = speed

    @property
    def left(self):
        """ Возващает координату x левой границы объекта """
        return self.bounds.left

    @property
    def right(self):
        """ Возващает координату x правой границы объекта """
        return self.bounds.right

    @property
    def top(self):
        """ Возващает координату y верхней границы объекта """
        return self.bounds.top

    @property
    def bottom(self):
        """ Возващает координату y нижней границы объекта """
        return self.bounds.bottom

    @property
    def width(self):
        """ Возващает ширину объекта """
        return self.bounds.width

    @property
    def height(self):
        """ Возващает высоту объекта """
        return self.bounds.height

    @property
    def center(self):
        """ Возвращает координаты центра объекта """
        return self.bounds.center

    @property
    def centerx(self):
        """ Возвращает координату x центра объекта """
        return self.bounds.centerx

    @property
    def centery(self):
        """ Возвращает координату y центра объекта """
        return self.bounds.centery

    def draw(self, surface):
        pass

    def move(self, dx, dy):
        """ Перемещает объект по оси OX на dx  и по оси OY на dy """
        self.bounds = self.bounds.move(dx, dy)

    def update(self):
        """ Обновляет информацию о перемещении объекта """
        if self.speed == [0, 0]:
            return
        self.move(*self.speed)
