"Магические методы - dunder (double underscore)"

class Computer:
    def __init__(self, name, ssd):   # Вызывается при создании класса 
        self.name = name
        self.ssd = ssd
    # def info(self):
    #     print(f'{self.name} память - {self.ssd}')

    # def __repr__(self):  # print
    #     return f'{self.name} память - {self.ssd} это репр'

    def __str__(self):
        return f'{self.name} память - {self.ssd} '
    

class MacBook(Computer):
    def __init__(self, name, ssd, cpu):
        super().__init__(name, ssd)
        self.cpu = cpu

    def __str__(self):
        return super().__str__() + f'процессор - {self.cpu}'

    def __call__(self, a, b):
        print("Hello World!")
        print(a + b)
    
    "Магические методы для арифметических действий"

    def __add__(self, other):      # +
        new_ssd = self.ssd + other.ssd
        return MacBook(self.name, new_ssd, self.cpu)
    def __sub__(self, other):      # +
        new_ssd = self.ssd - other.ssd
        return MacBook(self.name, new_ssd, self.cpu)
    def __mul__(self, other):      # *
        new_ssd = self.ssd * other.ssd
        return MacBook(self.name, new_ssd, self.cpu)
    def __floordiv__(self, other):      # //
        new_ssd = self.ssd // other.ssd
        return MacBook(self.name, new_ssd, self.cpu)
    def __truediv__(self, other):      # /
        new_ssd = self.ssd / other.ssd
        return MacBook(self.name, new_ssd, self.cpu)

    "Магические методы для операторов сравнения"

    def __gt__(self, other):  # больше чем ( > )
        return self.ssd > other.ssd
    def __lt__(self, other):  # меньше чем ( < )
        return self.ssd < other.ssd
    def __eq__(self, other):  # равен ( == )
        return self.ssd == other.ssd
    def __ne__(self, other):  # не равен ( != )
        return self.ssd == other.ssd
    def __ge__(self, other):  # больше или равно ( >= )
        return self.ssd >= other.ssd
    def __le__(self, other):  # меньше или равно ( <= )
        return self.ssd <= other.ssd
mac = MacBook("macbook a11", 512, "M1")
mac_2 = MacBook("macbook air", 512, "M2")
# print(mac + mac_2)
# print(mac - mac_2)
# print(mac * mac_2)
# print(mac // mac_2)
# print(mac / mac_2)
# print(mac > mac_2)
# print(mac < mac_2)
# print(mac == mac_2)
# print(mac >= mac_2)
# print(mac >= mac_2)


# print(mac)
# mac(3, 32) 
# lenovo = Computer("Lenovo", 512)
# lenovo.info()
# print(lenovo)


