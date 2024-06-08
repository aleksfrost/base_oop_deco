import time

from random import randint


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Время выполнения функции {func.__name__}: {end - start:.6f}")
        return result
    return wrapper


def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        print("Функция вызвана с параметрами:")
        print(args, kwargs)
        return result

    return wrapper


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """
    count = 0
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    count = count + 1
    print(f"Функция была вызвана: {count} раз")

    return wrapper