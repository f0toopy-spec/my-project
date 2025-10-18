class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"Transport is moving at {self.speed} km/h")

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"


class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats

    def honk(self):
        print("Beep beep!")

    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"

    def __len__(self):
        return self.seats

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False

    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        return NotImplemented


class Bike(Transport):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.type = bike_type

    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")

    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}, Type: {self.type}"


# 4. Практика использования
print("=== 4. Практика использования ===")

# 1. Создание объектов
transport = Transport("Generic", 80)
car1 = Car("Toyota", 120, 5)
car2 = Car("Honda", 100, 7)
bike = Bike("Giant", 25, "mountain")

# 2. Вывод на экран
print("\n1. Вывод объектов:")
print(transport)
print(car1)
print(car2)
print(bike)

# 3. Проверка методов move() и honk()
print("\n2. Методы move() и honk():")
transport.move()
car1.move()
car2.move()
bike.move()
car1.honk()
car2.honk()

# 4. Использование len(car)
print(f"\n3. Количество мест в car1: {len(car1)}")
print(f"Количество мест в car2: {len(car2)}")

# 5. Сравнение двух машин
print(f"\n4. Сравнение машин: car1 == car2: {car1 == car2}")

# 6. Сложение скоростей двух машин
print(f"\n5. Сумма скоростей car1 и car2: {car1 + car2} km/h")

# 7. Сложение машины и велосипеда
print("\n6. Сложение машины и велосипеда:")
try:
    result = car1 + bike
    print(f"Результат: {result}")
except TypeError as e:
    print(f"Ошибка: {e}")
    print("Объяснение: Метод __add__ в классе Car проверяет, является ли второй объект экземпляром Car.")
    print("Если нет - возвращается NotImplemented, что вызывает TypeError.")

# 5. Дополнительное задание
print("\n=== 5. Дополнительное задание ===")

# Создание списка объектов
vehicles = [
    Transport("Generic", 60),
    Car("BMW", 180, 4),
    Car("Mercedes", 160, 5),
    Bike("Trek", 30, "road"),
    Bike("Specialized", 20, "mountain")
]

print("Вызов метода move() для всех объектов в списке:")
for vehicle in vehicles:
    vehicle.move()



