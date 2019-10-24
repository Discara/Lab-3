# from lab_python_oop import *
from circle import Circle
from rectangle import Rectangle
from square import Square

def main():
    print('\n')
    Square1 = Square(5, "красный")
    Square1.repr()
    print('\n')
    Circle1 = Circle(5, "зеленый")
    Circle1.repr()
    print('\n')
    Rect1 = Rectangle(2, 3, "синий")
    Rect1.repr()

if __name__ == "__main__":
    # execute only if run as a script
    main()

