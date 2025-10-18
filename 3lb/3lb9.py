from datetime import datetime, date, timedelta


def get_manual_date():

    print("\n--- Ввод текущей даты ---")
    print("Выберите вариант:")
    print("1 - Использовать системную дату")
    print("2 - Ввести дату вручную")

    choice = input("Ваш выбор (1 или 2): ")

    if choice == "2":
        try:
            year = int(input("Введите год: "))
            month = int(input("Введите месяц: "))
            day = int(input("Введите день: "))

            manual_date = date(year, month, day)
            print(f"Установлена дата: {manual_date.strftime('%d.%m.%Y')}")
            return manual_date

        except ValueError as e:
            print(f"Ошибка ввода даты: {e}")
            print("Используется системная дата")
            return date.today()
    else:
        today = date.today()
        print(f"Используется системная дата: {today.strftime('%d.%m.%Y')}")
        return today


def birthday_calculator_with_manual_date():

    print("=== Калькулятор дней рождения ===")


    print("\n--- Ввод даты рождения ---")
    try:
        birth_year = int(input("Введите год рождения: "))
        birth_month = int(input("Введите месяц рождения: "))
        birth_day = int(input("Введите день рождения: "))

        birthday = date(birth_year, birth_month, birth_day)
    except ValueError as e:
        print(f"Ошибка ввода даты рождения: {e}")
        return

    current_date = get_manual_date()

    print(f"\nДата рождения: {birthday.strftime('%d.%m.%Y')}")
    print(f"Текущая дата: {current_date.strftime('%d.%m.%Y')}")
    print()

    if birthday > current_date:
        print("Ошибка: Дата рождения не может быть позже текущей даты!")
        return


    days_passed = (current_date - birthday).days
    print(f"1. Дней прошло с момента рождения: {days_passed:,} дней")

    next_birthday = date(current_date.year, birthday.month, birthday.day)


    if next_birthday < current_date:
        next_birthday = date(current_date.year + 1, birthday.month, birthday.day)

    days_to_birthday = (next_birthday - current_date).days

    print(f"2. Дней до следующего дня рождения: {days_to_birthday} дней")
    print(f"   Следующий день рождения: {next_birthday.strftime('%d.%m.%Y')}")


def detailed_calculation_with_manual_date():

    print("\n" + "=" * 50)
    print("=== Подробный расчет ===")

    try:
        birth_year = int(input("Введите год рождения: "))
        birth_month = int(input("Введите месяц рождения: "))
        birth_day = int(input("Введите день рождения: "))

        birthday = date(birth_year, birth_month, birth_day)
    except ValueError:
        print("Ошибка: Введите корректные числовые значения для даты рождения!")
        return

    current_date = get_manual_date()

    if birthday > current_date:
        print("Ошибка: Дата рождения не может быть позже текущей даты!")
        return

    print(f"\nДата рождения: {birthday.strftime('%d.%m.%Y')}")
    print(f"Текущая дата: {current_date.strftime('%d.%m.%Y')}")


    total_days = (current_date - birthday).days
    print(f"\nВсего дней с рождения: {total_days:,}")


    years = total_days // 365
    remaining_days = total_days % 365
    months = remaining_days // 30
    days = remaining_days % 30

    print(f"Это примерно: {years} лет, {months} месяцев, {days} дней")


    next_birthday = date(current_date.year, birthday.month, birthday.day)
    if next_birthday <= current_date:
        next_birthday = date(current_date.year + 1, birthday.month, birthday.day)

    days_to_next = (next_birthday - current_date).days

    print(f"\nСледующий день рождения: {next_birthday.strftime('%d.%m.%Y')}")
    print(f"Дней до следующего дня рождения: {days_to_next}")


    if days_to_next == 0:
        print("С ДНЕМ РОЖДЕНИЯ!")
    elif days_to_next == 1:
        print("Завтра ваш день рождения! ")
    elif days_to_next <= 7:
        print(f"До дня рождения осталась всего {days_to_next} дней!")


def future_date_calculation():

    print("\n" + "=" * 50)
    print("=== Расчет для будущих дат ===")

    print("Введите целевую дату (к которой нужно посчитать дни):")
    try:
        target_year = int(input("Год: "))
        target_month = int(input("Месяц: "))
        target_day = int(input("День: "))

        target_date = date(target_year, target_month, target_day)
    except ValueError:
        print("Ошибка ввода целевой даты!")
        return

    current_date = get_manual_date()

    print(f"\nТекущая дата: {current_date.strftime('%d.%m.%Y')}")
    print(f"Целевая дата: {target_date.strftime('%d.%m.%Y')}")


    if target_date > current_date:
        days_difference = (target_date - current_date).days
        print(f"До целевой даты осталось: {days_difference} дней")
    elif target_date < current_date:
        days_difference = (current_date - target_date).days
        print(f"С целевой даты прошло: {days_difference} дней")
    else:
        print("Целевая дата совпадает с текущей!")



if __name__ == "__main__":
    while True:
        print("\n" + "=" * 60)
        print("ГЛАВНОЕ МЕНЮ")
        print("1 - Основной расчет дней рождения")
        print("2 - Подробный расчет")
        print("3 - Расчет дней до будущей даты")
        print("4 - Выход")

        choice = input("Выберите опцию (1-4): ")

        if choice == "1":
            birthday_calculator_with_manual_date()
        elif choice == "2":
            detailed_calculation_with_manual_date()
        elif choice == "3":
            future_date_calculation()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")