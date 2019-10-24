from geom_figure import GeometricFigure
from figure_color import FigureColor
import math

class Circle(GeometricFigure):

    def __init__(self, radius, color):
        self.radius = radius
        figure_color = FigureColor()
        figure_color.set_color(color)
        self.color = figure_color.get_color()
        self.name = 'Круг'

    def area(self, r):
        return math.pi*r*r

    def repr(self):
        print('Название фигуры: {}'.format(self.name))
        print('Радиус круга = {}'.format(self.radius))
        print('Площадь круга = {}'.format(self.area(self.radius)))
        print('Цвет круга: {}'.format(self.color))
