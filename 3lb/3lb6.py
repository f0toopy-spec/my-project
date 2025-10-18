from decimal import Decimal, getcontext


def deposit_calculator():

    getcontext().prec = 20

    try:
        start_money = Decimal(input("Введите начальную сумму вклада (рубли.копейки): "))
        percent = Decimal(input("Введите годовую процентную ставку (например, 7.5): "))
        years_count = Decimal(input("Введите срок вклада в годах: "))
    except:
        print("Ошибка ввода! Проверьте правильность введенных данных.")
        return

    if start_money <= 0 or percent <= 0 or years_count <= 0:
        print("Все значения должны быть положительными!")
        return
    month_percent = percent / (Decimal('12') * Decimal('100'))
    total_months = Decimal('12') * years_count
    growth = (Decimal('1') + month_percent) ** total_months
    end_money = start_money * growth
    end_money = end_money.quantize(Decimal('0.01'))
    earned_money = end_money - start_money
    print("РЕЗУЛЬТАТЫ РАСЧЕТА:")
    print(f"Начальная сумма: {start_money} руб.")
    print(f"Годовая ставка: {percent}%")
    print(f"Срок вклада: {years_count} лет")
    print(f"Итоговая сумма: {end_money} руб.")
    print(f"Общая прибыль: {earned_money} руб.")
    print("=" * 50)
if __name__ == "__main__":
    deposit_calculator()