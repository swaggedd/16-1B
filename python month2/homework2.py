# 1.	Создать класс Person с атрибутами fullname, age, is_married
# 2. Добавить в класс Person метод introduce_myself(представиться), который бы распечатывал всю информацию о человеке

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f'Fullname: {self.fullname}')
        print(f'Age: {self.age}')
        print(f'Status: {self.is_married}')
person1 = Person("Rustam", 16, "Isn't Married")
person1.introduce_myself()


# 3.	Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом объекта experience.
# Доп. Задание:
# 1. Добавить в класс Teacher атрибут класса salary = 0
# 2. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 3000 за каждый год опыта.
# 3. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату

class Teacher(Person):
    salary = 0
    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience
    
    def salary(self):
        bonus = 3000 * self.experience
        self.salary = 30000 + bonus

    def introduce_myself(self):
        Person.introduce_myself(self)
        print(f"Experience: {self.experience} years")
        print(f'Salary: {self.salary}')
teacher1 = Teacher("Ann", 40, "isn't married", 15)
teacher1.salary()
teacher1.introduce_myself()

