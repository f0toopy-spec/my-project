print("Таблица умножения:")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} × {j} = {i*j}\t", end="")
    print()
sum_odd = 0
for i in range(1, 101, 2):
    sum_odd += i
print(f"Сумма нечётных чисел от 1 до 100: {sum_odd}")
n = int(input("Введите число: "))
y=[]
for i in range(1, n + 1):
    if n % i == 0:
      y.append(i)
print(f"Делители: {y}")
n = int(input("Введите число для вычисления факториала: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факториал числа {n} = {factorial}")
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib



n = int(input("Введите длину последовательности Фибоначчи: "))
print(f"Последовательность Фибоначчи: {fibonacci(n)}")
import random

# 0. Подготовка цикла из случайных чисел
numbers = [random.randint(-50, 50) for i in range(10)]
print(f"Исходный список: {numbers}")

# 1. Чётные элементы
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Чётные элементы: {even_numbers}")

# 2. Максимальное и минимальное число
print(f"Максимальное: {max(numbers)}, Минимальное: {min(numbers)}")

# 3. Пользовательский ввод
user_numbers = []
for i in range(5):
    num = int(input(f"Введите число {i+1}: "))
    user_numbers.append(num)
user_numbers.sort()
print(f"Отсортированный список: {user_numbers}")

# 4. Удаление дубликатов
unique_list = []
for item in numbers:
    if item not in unique_list:
        unique_list.append(item)
print(f"Список без дубликатов: {unique_list}")

# 5. Поменять местами первый и последний
if len(numbers) >= 2:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(f"После замены: {numbers}")
students = {
    "Иван": 85,
    "Николай": 92,
    "Евгений": 78,
    "Себастьян": 95,
    "Сергей": 88
}

average_score = sum(students.values()) / len(students)
print(f"Средний балл: {average_score}")
text = input("Введите строку: ").lower()
letter_count = {}

for char in text:
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1

print("Количество букв:")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")
squares = {i: i**2 for i in range(1, 11)}
print(squares)
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

result_dict = dict(zip(keys, values))
print(result_dict)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Множество 1: {set1}")
print(f"Множество 2: {set2}")
print(f"Пересечение: {set1 & set2}")
print(f"Объединение: {set1 | set2}")
text = input("Введите текст: ").lower()
words = text.split()
unique_words = set(words)

print(f"Уникальные слова: {unique_words}")
print(f"Количество уникальных слов: {len(unique_words)}")
list1 = [1, 2, 3, 4, 5, 2, 3]
list2 = [4, 5, 6, 7, 8, 4, 5]

common_elements = set(list1) & set(list2)
print(f"Общие элементы: {common_elements}")
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print(f"set_a является подмножеством set_b: {set_a.issubset(set_b)}")
print(f"set_b является подмножеством set_a: {set_b.issubset(set_a)}")
numbers_set = {5, 12, 8, 3, 15, 7, 10}
threshold = int(input("Введите число: "))


filtered_set = {x for x in numbers_set if x >= threshold}

print(f"Исходное множество: {numbers_set}")
print(f"Отфильтрованное множество: {filtered_set}")
import random
#Сгенерировать список из 20 случайных чисел и вывести только уникальные значения
random_numbers = [random.randint(1, 10) for i in range(20)]
unique_numbers = [num for num in random_numbers if random_numbers.count(num) == 1]
print(f"Исходный список: {random_numbers}")
print(f"Уникальные значения: {unique_numbers}")
#Создать словарь, где ключи – это элементы списка, а значения – количество их повторений.
items = ['собака ', 'бурундук', 'карта', 'карта', 'обезьяна', 'обезьяна']
count_dict = {}

for item in items:
    count_dict[item] = count_dict.get(item, 0) + 1

print(count_dict)
#Дан список слов. Создать множество из слов, длина которых больше 5 символов.
words = ['самолёт', 'бумага', 'кот', 'карась', 'трава', 'дом', 'блок']
long_words = {word for word in words if len(word) > 5}

print(long_words)

#Ввести предложение. Сохранить в словарь количество вхождений каждого слова.
sentence = input("Введите предложение: ").lower().split()
word_count = {}

for word in sentence:
    word = word.strip('.,!?;:')
    if word:
        word_count[word] = word_count.get(word, 0) + 1

print("Количество вхождений слов:")
for word, count in word_count.items():
    print(f"{word}: {count}")



#Создать список чисел, преобразовать его в множество и обратно в список (убрав дубликаты).
numbers = [1, 2, 3, 3, 4, 3, 5, 1, 5, 1]
unique_numbers = list(set(numbers))

print(f"Исходный список: {numbers}")
print(f"Список без дубликатов: {unique_numbers}")

#Дан словарь "товар – цена". Найти самый дорогой товар.
products = {
    'водка': 450,
    'пиво': 80,
    'сыр': 300,
    'колбаса': 250,
    'коньяк': 920
}

most_expensive = max(products, key=products.get)
print(f"Самый дорогой товар: {most_expensive} - {products[most_expensive]} руб.")


#Дан список имён. Определить, какие из имён встречаются более одного раза. Какое имя встречается чаще всего.
names = ['Александр', 'Алексей', 'Артемий', 'Александр', 'Анна', 'Алексей', 'Афанасий']


duplicate_names = {name for name in names if names.count(name) > 1}
print(f"Имена, встречающиеся более одного раза: {duplicate_names}")


most_common = max(set(names), key=names.count)
print(f"Самое частое имя: {most_common} (встречается {names.count(most_common)} раз)")


#Запросить у пользователя строку и составить словарь: символ  индекс его первого вхождения.
text = input("Введите строку: ")
first_occurrence = {}

for index, char in enumerate(text):
    if char not in first_occurrence:
        first_occurrence[char] = index

print("Первый индекс вхождения каждого символа:")
for char, index in first_occurrence.items():
    print(f"'{char}': {index}")