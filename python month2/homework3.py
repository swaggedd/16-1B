# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
# 2. Добавить в класс Computer приватный метод make_computations, в котором бы выполнялись арифметические вычисления(‘+’,  ‘-’,  ‘*’,  ‘/’ ) с атрибутами объекта cpu и memory результат вывести красиво с помощью ‘ f ’ .
# 3. Добавить геттеры к существующим атрибутам.

class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory       

    
    def __make_computations(self, operation):
        if operation == "+":
            print(f'{self.__cpu} + {self.__memory} = {self.__cpu + self.__memory}')
        elif operation == "-":
            print(f'{self.__cpu} - {self.__memory} = {self.__cpu - self.__memory}')
        elif operation == "/":
            print(f'{self.__cpu} / {self.__memory} = {self.__cpu / self.__memory}')
        elif operation == "*":
            print(f'{self.__cpu} * {self.__memory} = {self.__cpu * self.__memory}')
        else:
            print("Ошибка")

    @property
    def get_make_computations(self):
        return self.__make_computations
    @property
    def get_cpu(self):
        return self.__cpu
    @property
    def get_memory(self):
        return self.__memory

    def info(self):
        print(f'Memory: {self.__memory}, CPU: {self.__cpu}')
# 4. Создать класс Laptop - который наследуется от класса Computer с приватным полем memory_card(карта памяти)
# 5. Добавить геттеры к существующему атрибуту.
# 6. Распечатать информацию о созданных объектах с помощью метода info
# 7. Опробовать все возможные методы каждого объекта
        
class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card
    @property
    def get_memory_card(self):
        return self.__memory_card

    def info(self):
        super().info()
        print(f'Memory card: {self.__memory_card}')


computer1 = Computer(8, 16)
computer1.info()
computer1.get_make_computations('+')


laptop1 = Laptop(2, 4, "SD")
laptop1.info()
laptop1.get_make_computations('*')

