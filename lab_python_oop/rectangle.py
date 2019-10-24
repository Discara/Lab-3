from geom_figure import GeometricFigure
from figure_color import FigureColor

class Rectangle(GeometricFigure):

    def __init__(self, width, length, color):
        self.width = width
        self.length = length
        figure_color = FigureColor()
        figure_color.set_color(color)
        self.color = figure_color.get_color()
        self.name = 'Прямоугольник'

    def area(self, a, b):
        return a * b

    def repr(self):
        print('Название фигуры: {}'.format(self.name))
        print('Стороны прямоугольника = {}, {}'.format(self.width, self.length))
        print('Площадь прямоугольника = {}'.format(self.area(self.width, self.length)))
        print('Цвет прямоугольника: {}'.format(self.color))
