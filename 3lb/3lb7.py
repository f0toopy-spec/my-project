from fractions import Fraction


def fraction_operations():
    print("=== Операции с дробями ===")

    fraction1 = Fraction(3, 4)
    fraction2 = Fraction(4, 6)

    print(f"Дробь 1: {fraction1}")
    print(f"Дробь 2: {fraction2}")
    print()


    addition = fraction1 + fraction2
    print(f"Сложение: {fraction1} + {fraction2} = {addition}")


    subtraction = fraction1 - fraction2
    print(f"Вычитание: {fraction1} - {fraction2} = {subtraction}")


    multiplication = fraction1 * fraction2
    print(f"Умножение: {fraction1} × {fraction2} = {multiplication}")


    division = fraction1 / fraction2
    print(f"Деление: {fraction1} ÷ {fraction2} = {division}")



def fraction_properties():
    print("\n=== Свойства дробей ===")

    fraction1 = Fraction(3, 4)
    fraction2 = Fraction(4, 6)

    print(f"Дробь {fraction1}:")
    print(f"  Числитель: {fraction1.numerator}")
    print(f"  Знаменатель: {fraction1.denominator}")

    print(f"Дробь {fraction2}:")
    print(f"  Числитель: {fraction2.numerator}")
    print(f"  Знаменатель: {fraction2.denominator}")


    print(f"\nПроверка на несократимость:")
    print(f"Дробь {fraction1} уже несократима: НОД({fraction1.numerator}, {fraction1.denominator}) = 1")
    print(f"Дробь {fraction2} уже несократима: НОД({fraction2.numerator}, {fraction2.denominator}) = 1")



if __name__ == "__main__":
    fraction_operations()
    fraction_properties()