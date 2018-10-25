# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

        self.length1 = float(((self.point2[0] - self.point1[0]) ** 2 + (self.point2[1] - self.point1[1]) ** 2) ** (1 / 2))
        self.length2 = float(((self.point3[0] - self.point2[0]) ** 2 + (self.point3[1] - self.point2[1]) ** 2) ** (1 / 2))
        self.length3 = float(((self.point3[0] - self.point1[0]) ** 2 + (self.point3[1] - self.point1[1]) ** 2) ** (1 / 2))

    # метод, который считает периметр
    def perimeter(self):

        # проверяем треугольник на треугольность
        if self.length1 + self.length2 > self.length3 and self.length2 + self.length3 > self.length1 and self.length1 + self.length3 > self.length2:
            return self.length1 + self.length2 + self.length3
        else:
            print("выршины предполагаемого треугольника лежат на одной прямой")
            return None

    # метод, который  вычисляет высоту
    def height(self):
        # высот в треугольнике ти, считаем все.

        try:
            h1 = 2 * self.square()/self.length2
            h2 = 2 * self.square()/self.length3
            h3 = 2 * self.square()/self.length1
            return [h1, h2, h3]

        except ZeroDivisionError:
            print("К сожалению, координаты предоставленных точек не являются вершинами треугольника")

    def square(self):
        # используем уже полученный периметр
        try:
            half_p = self.perimeter() / 2
            return (half_p * (half_p - self.length2) * (half_p - self.length3) * (half_p - self.length1)) ** (1 / 2)

        except Exception:
            print("К сожалению, координаты предоставленных точек не являются вершинами треугольника")
            return None

# тестовые данные:
# треугольный треугольник

p1 = Triangle([0, 0], [3, 0], [0, 4])
print("Периметр: ", p1.perimeter(), "Площадь:", p1.square(), "Набор высот:", p1.height())

# не треугольник
p2 = Triangle([0, 0], [0, 4], [0, 5])
print("Периметр: ", p2.perimeter(), "Площадь:", p2.square(), "Набор высот:", p2.height())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

from math import sqrt

class HipsTrapez:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        # вычисляем предполагаемые стороны трапеции
        self.length1 = float(((self.point2[0] - self.point1[0]) ** 2 + (self.point2[1] - self.point1[1]) ** 2) ** (1 / 2))
        self.length2 = float(((self.point3[0] - self.point2[0]) ** 2 + (self.point3[1] - self.point2[1]) ** 2) ** (1 / 2))
        self.length3 = float(((self.point3[0] - self.point4[0]) ** 2 + (self.point3[1] - self.point4[1]) ** 2) ** (1 / 2))
        self.length4 = float(((self.point1[0] - self.point4[0]) ** 2 + (self.point1[1] - self.point4[1]) ** 2) ** (1 / 2))

        #  вычисляем предполагаемые диагонали трапеции:
        self.diagonal1 = float(((self.point3[0] - self.point1[0]) ** 2 + (self.point3[1] - self.point1[1]) ** 2) ** (1 / 2))
        self.diagonal2 = float(((self.point4[0] - self.point2[0]) ** 2 + (self.point4[1] - self.point2[1]) ** 2) ** (1 / 2))

        print("Длины возможной трапеции:  ", self.length1, self.length2, self.length3, self.length4)
        print("Диагонали возможной трапеции:  ", self.diagonal1, self.diagonal2)

    """ Метод, проверяющий трапецию на равнобокость: в равнобедренной трапеции равны диагонали и равны две стороны.
    """
    def check_hips(self):
        if self.length1 == self.length3 and self.length2 != self.length4 or  self.length2 == self.length4 and self.length1 != self.length3:
            if self.diagonal1 == self.diagonal2:

                print("Это равнобедренная трапеция")
                return True
        else:
            print("Это не равнобедренная трапеция")
            return False

# Вычисляем периметр:

    def perimeter(self):

        return self.length1 + self.length2 + self.length3 + self.length4

# Найдем площадь трапеции через высоту
    def square(self):
        if self.length1 == self.length3 and self.length2 != self.length4:

            # расстояние от основания высоты до ближайшей вершины
            a = (abs(self.length2 - self.length4))/2

            # вычисляем высоту
            h = sqrt((self.length1**2) - a**2)

            return h*(self.length2 + self.length4)/2

        elif self.length2 == self.length4 and self.length1 != self.length3:

            a = (abs(self.length1 - self.length3)) / 2

            # вычисляем высоту

            h = sqrt((self.length2 ** 2) - a ** 2)

            return h * (self.length1 + self.length3) / 2

        else:
            print("Это не равнобедренная трапеция")

            return None


# пример равнобедренной трапеции

trap1 = HipsTrapez([0, 0], [1, 4], [5, 4], [6, 0])
print("Проверка на равнобедренность и трапезоидность:", trap1.check_hips(), "Периметр: ", trap1.perimeter(), "Площадь:", trap1.square())


# пример неравнобедренной трапеции

trap2 = HipsTrapez([0, 0], [2, 4], [5, 4], [6, 0])
print("Проверка на равнобедренность и трапезоидность:", trap2.check_hips(), "Периметр: ", trap2.perimeter(), "Площадь:", trap2.square())
