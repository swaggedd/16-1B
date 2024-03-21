# Исключения try, except

# try:
#     print(geeks)    
# except NameError:
#     print("Нет переменной которую вы вызываете!")

# try:
#     print(100 / 0)
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")

# while True:
#     try:
#         a = int(input("Введите первое число: " ))
#         b = int(input("Введите второе число: "))
#         c = input("Введите знак: ")
#         d = int(input(("Нажмите ноль чтобы выйти из калькулятора: ")))
#         if c == "/":
#             try:
#                 print(f'{a} / {b} = {a/b}')
#             except ZeroDivisionError:
#                 print("На ноль делить нельзя!")
#         elif c == "+":
#             print(f'{a} + {b} = {a+b}')
#         elif c == "*":
#             print(f'{a} * {b} = {a*b}')
#         elif c == "-":
#             print(f'{a} - {b} = {a-b}')
#         elif d == 0:
#             break
#         else:
#             print("Неверное значение!")
#     except ValueError:
#         print("Вводить можно только целые числа int!")

        
# try:
#     lst = ["Hello", "World", "Geeks"]
#     print(lst[3])
# except Exception as error:
#     print("Возникла ошибка", error)

# raise OSError("Специально вызываем ошибку с оператором raise")



# Множества set и frozenset
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [3, 4, 5, 6, 7]
print(numbers1 + numbers2)
print(set(numbers1 + numbers2)) 


names = {"Islam", "Nurboolot", "Timur", "Syimyk", "Timur"}
print(names)

brands = {"Apple", "Asus", "HP", "Xiaomi", "MI", "Samsung", "HP"}
print(brands)
brands.add("Zara")
brands.remove("Apple")
brands.pop()
brands.clear()
print(brands)

# frozenset
frzn = frozenset({10, 20, 30, 40, 50, 60})
print(frzn)

# СЛОВАРИ dictionary (ключи и значения)


student = {'name': 'Aktan', 'age':'16'}
print(student)
print(type(student))
print(student["name"]) 
print(student["age"]) 
student.setdefault("language", "JavaScript")
print(student)