# Dictionary - Словари

numbers = {10, 20, 30, 40, 50, 10, 20, 30}
print(numbers)


language = {'name': 'Python', 'version': '3.10.8'}
print(language)
print(language["name"]) 
print(language["version"])


xiaomi_redmi_12 = {
    "id" : 281,
    "title" : "Xiaomi Redmi 12 6/128GB",
    "color" : "Black",
    "price" : 17090,
    "description" : "Xiaomi Redmi 12 6/128GB Black Osh"
}
print(xiaomi_redmi_12)
print("Название: ", xiaomi_redmi_12["title"])
print("Цвет: ", xiaomi_redmi_12["color"])
print("Цена: ", xiaomi_redmi_12["price"])
print("Описание: ", xiaomi_redmi_12["description"])


student = {"name" : "Musulmankul", "age" : 19}
print(student)
student.setdefault("address", "Mkr Toloikon")
print(student)
student.setdefault("language", "JavaScript")
print(student)
student["language"] = "Python"
print(student)
student["expirience"] = "3 months"
print(student)
student.pop("address")
print(student)
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)

# Функции - functions

def hello():
    print("Hello World!")
# hello()
def add():
    print(100 + 222)
# add()

def mult():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(num1 + num2)
# mult()

def div(number1, number2):
    print(number1 / number2)
# div(2, 3)

def welcome (name:str):
    print("Здравствуйте,", name)
# welcome("Rustam")
# welcome(1000)

def add(num1:int=1, num2:int=1) -> int:
    "Эта функция делает сложение двух чисел"
    print(num1+num2)
add()
add(5, 5)
add(100)