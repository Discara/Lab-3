class FigureColor:
    def __init__(self):
        self.color = None

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value  # ?

    def del_color(self):
        del self._color

    color = property(get_color, set_color, del_color, 'Color here')