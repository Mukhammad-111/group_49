class Figure:
    unit = 'cm'
    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(f'Square side length: {self.__side_length}{self.unit},'
              f' area:{self.calculate_area()}{self.unit}')

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f'Rectangle length: {self.__length}{self.unit}, '
              f'width: {self.__width}{self.unit}, '
              f'area: {self.calculate_area()}{self.unit}')

square_1 = Square(8)
square_2 = Square(4)
rectangle_1 = Rectangle(5, 7)
rectangle_2 = Rectangle(6, 9)
rectangle_3 = Rectangle(4, 11)
figures_list = [square_1, square_2, rectangle_1, rectangle_2, rectangle_3]
for figure in figures_list:
    figure.info()
