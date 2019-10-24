from rectangle import Rectangle
from figure_color import FigureColor

class Square(Rectangle):
    def __init__(self, side, color):
        self.side = side
        figure_color = FigureColor()
        figure_color.set_color(color)
        self.color = figure_color.get_color()
        self.name = 'Квадрат'

    def area(self, side):
        area = side*side
        return area

    def repr(self):
        print('Название фигуры: {}'.format(self.name))
        print('Сторона квадрата = {}'.format(self.side))
        print('Площадь квадрата = {}'.format(self.area(self.side)))
        print('Цвет квадрата: {}'.format(self.color))
