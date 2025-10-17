def logger(func):
    def wrapper(*args, **kwargs):
        # Логирование перед вызовом функции
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")

        # Вызов оригинальной функции
        result = func(*args, **kwargs)

        # Логирование после выполнения функции
        print(f"Функция {func.__name__} вернула {result}")

        return result

    return wrapper


# Применение декоратора к функциям

@logger
def add(a, b):
    """Возвращает сумму двух чисел"""
    return a + b


@logger
def divide(a, b):
    """Возвращает результат деления с обработкой деления на ноль"""
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


@logger
def greet(name):
    """Выводит приветствие"""
    return f"Привет, {name}!"


# Тестирование функций
if __name__ == "__main__":
    print("=== Тестирование функции add ===")
    result1 = add(5, 3)
    print(f"Результат: {result1}\n")

    print("=== Тестирование функции divide ===")
    result2 = divide(10, 2)
    print(f"Результат: {result2}\n")

    result3 = divide(8, 0)
    print(f"Результат: {result3}\n")

    print("=== Тестирование функции greet ===")
    result4 = greet("Анна")
    print(f"Результат: {result4}\n")

    # Дополнительные тесты с именованными аргументами
    print("=== Тестирование с именованными аргументами ===")
    result5 = add(a=7, b=4)
    print(f"Результат: {result5}")


def require_role(allowed_roles):
    """
    Декоратор, который проверяет роль пользователя перед выполнением функции
    """

    def decorator(func):
        def wrapper(user, *args, **kwargs):
            # Проверяем, есть ли роль пользователя в списке разрешенных ролей
            if user.get('role') in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещен пользователю {user['name']}")
                return None

        return wrapper

    return decorator


# Примеры использования декоратора

@require_role(['admin'])
def delete_database(user):
    """Удаление базы данных - доступно только администраторам"""
    print(f"База данных удалена пользователем {user['name']}")
    return "База данных успешно удалена"


@require_role(['admin', 'manager'])
def edit_settings(user):
    """Редактирование настроек - доступно администраторам и менеджерам"""
    print(f"Настройки изменены пользователем {user['name']}")
    return "Настройки успешно изменены"


@require_role(['admin', 'manager', 'user'])
def view_data(user):
    """Просмотр данных - доступно всем пользователям"""
    print(f"Данные просмотрены пользователем {user['name']}")
    return "Данные успешно загружены"


@require_role(['admin'])
def restart_server(user):
    """Перезагрузка сервера - доступно только администраторам"""
    print(f"Сервер перезагружен пользователем {user['name']}")
    return "Сервер успешно перезагружен"


# Создаем пользователей с разными ролями
users = [
    {'name': 'Алексей', 'role': 'admin'},
    {'name': 'Мария', 'role': 'manager'},
    {'name': 'Иван', 'role': 'user'},
    {'name': 'Ольга', 'role': 'guest'},
    {'name': 'Петр', 'role': 'admin'}
]

# Тестирование функций
if __name__ == "__main__":
    print("=== Тестирование декоратора доступа ===\n")

    # Тестируем каждую функцию для каждого пользователя
    functions_to_test = [
        ("Удаление базы данных", delete_database),
        ("Редактирование настроек", edit_settings),
        ("Просмотр данных", view_data),
        ("Перезагрузка сервера", restart_server)
    ]

    for function_name, function in functions_to_test:
        print(f"--- {function_name} ---")
        for user in users:
            print(f"Пользователь: {user['name']} (роль: {user['role']})")
            result = function(user)
            if result:
                print(f"Результат: {result}")
            print()
        print("=" * 50)

    # Дополнительное тестирование с разными сценариями
    print("\n=== Дополнительные тесты ===\n")

    # Тест с пользователем без роли
    user_without_role = {'name': 'Безрольный'}
    print("Тест пользователя без роли:")
    delete_database(user_without_role)
    print()


    # Тест с расширенными параметрами функций
    @require_role(['admin', 'manager'])
    def create_user(current_user, new_user_name, new_user_role):
        """Создание нового пользователя"""
        print(
            f"Пользователь {current_user['name']} создал нового пользователя: {new_user_name} с ролью: {new_user_role}")
        return f"Пользователь {new_user_name} создан"


    print("Тест функции с дополнительными параметрами:")
    admin_user = {'name': 'Администратор', 'role': 'admin'}
    result = create_user(admin_user, "Новый пользователь", "user")
    print(f"Результат: {result}\n")

    manager_user = {'name': 'Менеджер', 'role': 'manager'}
    result = create_user(manager_user, "Еще один пользователь", "user")
    print(f"Результат: {result}\n")

    regular_user = {'name': 'Обычный', 'role': 'user'}
    result = create_user(regular_user, "Неавторизованный", "user")
    print()