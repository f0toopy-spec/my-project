def fibonacci(n):

    a, b = 0, 1
    count = 0

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def demo_fibonacci():
    print("=== Генератор чисел Фибоначчи ===")

    print("Первые 5 чисел Фибоначчи (первый вызов):")
    for num in fibonacci(5):
        print(num, end=" ")
    print()

    print("Первые 5 чисел Фибоначчи (второй вызов):")
    for num in fibonacci(5):
        print(num, end=" ")
    print()


    print("\nПервые 10 чисел Фибоначчи:")
    for num in fibonacci(10):
        print(num, end=" ")
    print()


    print("\nПервые 8 чисел Фибоначчи как список:")
    fib_list = list(fibonacci(8))
    print(fib_list)







if __name__ == "__main__":
    demo_fibonacci()



