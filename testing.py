import math
message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень"""
    return math.sqrt(Number)


def calc(your_number):
    if your_number <= 0:
        return 0

    print(f'Мы вычислили квадратный корень из введённого'
          f' вами числа. Это будет: {CalculateSquareRoot(your_number)}')
