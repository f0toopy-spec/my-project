from datetime import datetime


def current_datetime_demo():


    now = datetime.now()

    print(f"Текущая дата и время: {now}")


    current_date = now.date()
    print(f"Только текущая дата: {current_date}")

    current_time = now.time()
    print(f"Только текущее время: {current_time}")


def formatted_datetime():

    print("\n=== Форматированный вывод ===")

    now = datetime.now()


    print("Форматированная дата и время:")
    print(f"  Полный формат: {now.strftime('%d.%m.%Y %H:%M:%S')}")
    print(f"  Дата: {now.strftime('%d.%m.%Y')}")
    print(f"  Время: {now.strftime('%H:%M:%S')}")


    print("\nАльтернативные способы:")
    from datetime import date, time

    today = date.today()
    current_time = datetime.now().time()

    print(f"Только дата (через date.today()): {today}")
    print(f"Только время (через datetime.now().time()): {current_time}")


def datetime_components():

    print("\n=== Компоненты даты и времени ===")

    now = datetime.now()

    print("Отдельные компоненты:")
    print(f"  Год: {now.year}")
    print(f"  Месяц: {now.month}")
    print(f"  День: {now.day}")
    print(f"  Час: {now.hour}")
    print(f"  Минута: {now.minute}")
    print(f"  Секунда: {now.second}")
    print(f"  Микросекунда: {now.microsecond}")


if __name__ == "__main__":
    current_datetime_demo()
    formatted_datetime()
    datetime_components()

