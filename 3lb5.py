from decimal import Decimal, getcontext


def deposit_calculator():
    # Устанавливаем точность вычислений
    getcontext().prec = 20

    print("=== Финансовый калькулятор вкладов ===")

    # Ввод данных с преобразованием в Decimal
    try:
        initial_amount = Decimal(input("Введите начальную сумму вклада (рубли.копейки): "))
        interest_rate = Decimal(input("Введите годовую процентную ставку (например, 7.5): "))
        years = Decimal(input("Введите срок вклада в годах: "))
    except:
        print("Ошибка ввода! Проверьте правильность введенных данных.")
        return

    # Проверка на положительные значения
    if initial_amount <= 0 or interest_rate <= 0 or years <= 0:
        print("Все значения должны быть положительными!")
        return

    # Расчет по формуле ежемесячной капитализации
    # S = P × (1 + r/(12×100))^(12×t)

    # Месячная ставка в десятичной форме
    monthly_rate = interest_rate / (Decimal('12') * Decimal('100'))

    # Количество периодов капитализации
    periods = Decimal('12') * years

    # Коэффициент наращения
    multiplier = (Decimal('1') + monthly_rate) ** periods

    # Итоговая сумма
    final_amount = initial_amount * multiplier

    # Округляем до копеек (2 знака после запятой)
    final_amount = final_amount.quantize(Decimal('0.01'))

    # Прибыль
    profit = final_amount - initial_amount

    # Вывод результатов
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ РАСЧЕТА:")
    print(f"Начальная сумма: {initial_amount} руб.")
    print(f"Годовая ставка: {interest_rate}%")
    print(f"Срок вклада: {years} лет")
    print(f"Итоговая сумма: {final_amount} руб.")
    print(f"Общая прибыль: {profit} руб.")
    print("=" * 50)


# Запуск калькулятора
if __name__ == "__main__":
    deposit_calculator()