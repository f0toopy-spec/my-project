# 1. Декоратор логирования

def logger(func):
    def wrapper(*args, **kwargs):
        # Перед вызовом функции
        print(f"Вызов функции {func.__name__} с аргументами: args={args}, kwargs={kwargs}")

        # Вызов оригинальной функции
        result = func(*args, **kwargs)

        # После вызова функции
        print(f"Функция {func.__name__} вернула: {result}")

        return result

    return wrapper


# 2. Декоратор замера времени выполнения

import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time:.4f} секунд")
        return result

    return wrapper


# 3. Декоратор кэширования (мемоизации)

def cache(func):
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Создаем ключ на основе аргументов
        key = (args, tuple(kwargs.items()))

        if key in cached_results:
            print(f"Используется кэшированный результат для {func.__name__}{args}")
            return cached_results[key]

        result = func(*args, **kwargs)
        cached_results[key] = result
        print(f"Результат для {func.__name__}{args} сохранен в кэш")
        return result

    return wrapper


# 4. Декоратор валидации аргументов

def validate_numbers(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Проверяем позиционные аргументы
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Аргумент {arg} должен быть числом")

        # Проверяем именованные аргументы
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"Аргумент {key}={value} должен быть числом")

        return func(*args, **kwargs)

    return wrapper


# Пример использования декораторов

@logger
@timer
def factorial(n):
    """Вычисляет факториал числа"""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


@cache
@validate_numbers
def fibonacci(n):
    """Вычисляет n-ное число Фибоначчи"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@timer
@validate_numbers
def power(base, exponent):
    """Возводит число в степень"""
    return base ** exponent


# Демонстрация работы

if __name__ == "__main__":


    print("\n1. Факториал с логированием и таймером:")
    result1 = factorial(5)
    print(f"Результат: {result1}")

    print("\n2. Числа Фибоначчи с кэшированием и валидацией:")
    result2 = fibonacci(10)
    print(f"fibonacci(10) = {result2}")

    print("\n3. Возведение в степень с таймером и валидацией:")
    result3 = power(2, 8)
    print(f"2^8 = {result3}")

    print("\n4. Проверка валидации (должна вызвать ошибку):")
    try:
        power("2", 8)
    except ValueError as e:
        print(f"Ошибка: {e}")