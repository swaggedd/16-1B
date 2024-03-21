# Домашнее Задание 
# Задание 1:
# Создайте класс Fruits c атрибутами - (name, color, weight)
# Создайте три объекта класса и с помощью метода выведите информацию о каждом фрукте 

class Fruits:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def info(self):
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Weight: {self.weight} grams")

fruit1 = Fruits("Apple", "Red", 150)
fruit2 = Fruits("Banana", "Yellow", 120)
fruit3 = Fruits("Orange", "Orange", 180)
fruit1.info()
fruit2.info()
fruit3.info()


# Задание 2:
# Создайте класс Car c атрибутами - (model, year, color)
# Создайте метод drive с входящим параметром city(город) который будет выводить текст (Машина - `модель вашей машины`  едет в  - `ваш город`)
# Доп. Задание:
# Улучшите класс Car:
# Добавьте атрибут fuel со значением 0
# Добавьте метод refuel который будет пополнять бак и 	поставьте ограничение - (за раз можно пополнить 	только на 40 литров) 
# Измените метод drive :
# 	Теперь он должен запрашивать не только город но и расстояние до этого города, так же учитывайте что 	машина  расходует 1л / 10км. Если у машины не хватит бензина доехать, то должна появится надпись которая 	будет предупреждать сколько км может проехать 	машина 

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.fuel = 0
    def drive(self, city, distance):
        fuel_needed = distance / 10 
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            print(f"Машина - {self.model} едет в - {city}")
        else:
            possible_distance = self.fuel * 10
            print(f'Машина {self.model} сможет проехать только {possible_distance}км')
    def refuel(self, liters):
        if liters <= 40:
            self.fuel += liters
            print("Вы успешно заправились!")
        else:
            print("За раз можно пополнять на 40 литров!")

car_info = Car("CLS63s AMG", "2014", "black")
car_info.refuel(30)
car_info.drive("Osh", 500)
