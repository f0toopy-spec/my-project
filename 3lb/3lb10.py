from datetime import datetime


def format_datetime_custom(dt):

    months_ru = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }

    day = dt.day
    month = months_ru[dt.month]
    year = dt.year
    time_str = dt.strftime("%H:%M")

    return f"Сегодня {day} {month} {year} года, время: {time_str}"


now = datetime.now()
print(format_datetime_custom(now))


example_date = datetime(2025, 9, 26, 5, 30)
print(format_datetime_custom(example_date))