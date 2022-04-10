# from __future__ import braces #Задание 3


def second():
    x = float

    try:
        x = 10.0 ** 309
    except OverflowError:
        print("Задание 2.0.\nБыло выявлено исключение выхода за пределы вещественного числа. Максимальное значение =",
              10.0 ** 308)

    print(
        "\nЗадание 2.1 - Записать число 42 десятью разными способами: \n42, 42.0, 42e0, -(-42), 42e+0, 42e-0, 0o52, 0x2A, 0b00101010, 0.42e2")
    print(42 == 42, 42.0 == 42, 42e0 == 42, -(-42) == 42, 42e+0 == 42, 42e-0 == 42, 0o52 == 42, 0x2A == 42,
          0b00101010 == 42, 0.42e2 == 42)


def third():
    print("\nЗадание 3:\n1) Вывод Hello world:")
    import __hello__
    print("2) Антигравитация:")
    import antigravity


def forth():
    x = 1
    x += x  # 2
    y = x + x  # 4
    x = y + y  # 8
    x += y  # 12
    print("Умножение 1 на 12 = ", x)

    x = 1
    x += x  # 2
    y = x + x  # 4
    x = y + y  # 8
    x += x  # 16
    print("Умножение 1 на 16 = ", x)

    x = 1
    y = x + x  # 2
    y = y + y  # 4
    y = y + y  # 8
    print("Умножение 1 на 16 = ", y - (x - y))

    x = 1
    y = x + x  # 2
    y = y + y  # 4
    z = y + y  # 8
    z = z + z  # 16
    z = z + z  # 32
    z -= y  # 28
    x += z  # 29
    print("Умножение 1 на 16 = ", x)


def sixth():
    # 0 = "meow" #1

    # x = 1 y = 2 #2

    # c #3

    x = "str"
    y = 0.3
    # res = x-y #4

    # if (x=="str"):
    # print(x) #5

    с = 0
    # y = y/с #6

    # y = math.asin(-1.2) #7

    # math.exp(200000) #8


def seven():
    x = 0.6
    y = 0.3
    x += y
    print(x == 0.9)


def naive_mul(x, y):
    r = 1
    for i in range(0, y - 1):
        x = x + r


if __name__ == '__main__':
    # second()
    # third()
    # forth()
    # sixth()
    # seven()

    """
    for x in range(0, 100):
        for y in range(0, 100):
            naive_mul(x, y)
    """

