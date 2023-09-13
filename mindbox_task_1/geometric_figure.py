from functools import reduce
from typing import NoReturn


# Напишите на C# или Python библиотеку для поставки внешним клиентам,
# которая умеет вычислять площадь круга по радиусу
# и треугольника по трем сторонам.
#
# Дополнительно к работоспособности оценим:
# Юнит-тесты
# Легкость добавления других фигур
# Вычисление площади фигуры без знания типа фигуры в compile-time
# Проверку на то, является ли треугольник прямоугольным


class Figure:
    """
    Геометрическая фигура
    Geometric_shape
    """
    # __names = {
    #     1: 'Line',
    #     2: 'Rectangle/Square/Rhombus/Parallelogram',
    #     3: 'Triangle',
    #     4: 'Quadrilateral',
    # }
    __figure_types = {
        'c': 'Circle',  # Круг
        'z': 'Polygonal chain',  # Ломаная линия
        1: 'Line',  # Отрезок
        2: 'Rectangle',  # Прямоугольник
        3: 'Triangle',  # Треугольник
        4: 'Quadrilateral',  # Четырёхугольник
        5: 'Pentagon',  # Пятиугольник
        6: 'Hexagon',  # Шестиугольник
    }

    def __init__(self):
        self.__radius: int | float | None = None
        self.__sides: tuple | None = None
        self.__figure_type: str | None = None

    @staticmethod
    def __check_length(sides: list | tuple) -> bool:
        """
        Проверка длин сторон:
        если длина самой длинной стороны меньше
        чем сумма длин остальных сторон, то True
        :param sides: list | tuple
        :return: bool
        """
        return sum(sides) - max(sides) > max(sides)

    @classmethod
    def __check_figure_type(cls, value: float | list | tuple,
                            key: str = 'polygon') -> str | None:
        """
        Определение типа фигуры
        :param value: float | list | tuple (radius or sides length)
        :param key: str (circle or polygon)
        :return: str | None (name)
        """
        if key == 'circle':
            if value > 0:
                return cls.__figure_types.get('c')
            raise AttributeError('Радиус должен быть больше 0')
        if key == 'polygon':
            if not all([i > 0 for i in value]):
                raise AttributeError('Длины сторон должны быть больше 0')

            if len(value) == 1:
                return cls.__figure_types.get(1)
            if len(value) == 2:
                return cls.__figure_types.get(2)
            if len(value) > 6:
                return 'Not Implemented/Не реализовано'
            if cls.__check_length(value):
                return cls.__figure_types.get(len(value))
            return cls.__figure_types.get('z')

    def set_radius(self, radius: int | float) -> NoReturn:
        if self.__sides is not None:
            raise AttributeError(
                f'У данной фигуры ({self.__figure_type}) не может быть радиуса'
                f' так как заданы стороны'
            )
        self.__figure_type = self.__check_figure_type(radius, 'circle')
        self.__radius = radius

    def set_sides(self, *sides: int | float) -> NoReturn:
        if self.__radius is not None:
            raise AttributeError(
                f'У данной фигуры ({self.__figure_type}) не может быть сторон'
                f' так как задан радиус'
            )
        self.__figure_type = self.__check_figure_type(sides, 'polygon')
        self.__sides = sides

    def is_right_triangle(self) -> bool | None:
        """
        Проверка - является ли треугольник прямоугольным.
        Если фигура не треугольник - возвращает None
        Is Right triangle.
        :return: bool | None
        """
        if self.__figure_type == self.__figure_types.get(3):
            sorted_sides = sorted(self.__sides)
            hypotenuse_square = sorted_sides[-1] ** 2
            cathets_squares_sum = sum(map(lambda s: s ** 2, sorted_sides[:-1]))
            return hypotenuse_square == cathets_squares_sum
        # Right_triangle
        return None

    @property
    def circle_radius(self) -> int | float:
        """
        Радиус круга
        :return: int | float
        """
        return self.__radius

    @property
    def figure_sides(self) -> tuple:
        """
        Длины сторон фигуры
        :return: tuple
        """
        return self.__sides

    @property
    def figure_type(self) -> str | None:
        """
        Тип фигуры
        :return: str | None
        """
        return self.__figure_type

    def __triangle_area(self):
        """
        Площадь треугольника по трём сторонам (Формула Герона)
        Heron's formula - area of a triangle
        :return: float
        """

        # sp - (semi_perimeter) полупериметр треугольника
        sp = sum(self.__sides) / 2
        return (sp * reduce(lambda x, y: x * y,
                            map(lambda side: sp - side, self.__sides))) ** 0.5

    def __rectangle_area(self) -> float:
        """
        Площадь прямоугольника
        Rectangle area
        :return: float
        """
        return reduce(lambda x, y: x * y, self.__sides)

    def figure_area(self) -> float | None:
        """
        Площадь фигуры
        Figure area
        :return: float | None
        """
        if self.__figure_type == self.__figure_types.get('z'):
            # у ломаной линии нет площади
            return None
        if len(self.__sides) == 2:
            return self.__rectangle_area()
        if len(self.__sides) == 3:
            return self.__triangle_area()
        if len(self.__sides) > 3:
            # Not Implemented/Не реализовано
            return None
        return None
