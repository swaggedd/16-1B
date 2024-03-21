# Цикл for 

# for i in range(100001):
#     print(i)

# for geeks in range(1,51):
#     print("Geeks", geeks)

# for num in range(1, 500, 2):
#     print(num)

# numbers = []
# for i in range(1, 200):
#     if i % 2 == 0:
#         numbers.append(i)
# print(numbers)



# employes = ["Islam", "Syimyk", "Aziz", "Urmat", "Ulan"]
# print(employes)
# print(f'Здравствуйте, {employes[0]}')
# print(f'Здравствуйте, {employes[1]}')
# print(f'Здравствуйте, {employes[2]}')
# print(f'Здравствуйте, {employes[3]}')
# print(f'Здравствуйте, {employes[4]}')

# for i in employes:       #Итерация по списку
#     print(f'Здравствуйте, {i}')



# brands = ["Apple", "Gucci", "LV", "Xiaomi", "Samsung"]
# print(brands)
# for i in brands:
#     print(type(i))

# numbers = [101, 202, 303, 5, 6, 7, 1, 34]
# for i in numbers:
#     if i % 2 == 0:
#         print(i, "четный")
#     else:
#         print(i, "нечетный")


# while

# num1 = 10
# num2 = 20
# while num2 > num1:
#     num1 += 1
#     print(num1)

# number = 0
# while True:
#     number += 1
#     print(number)
#     if number > 100:
#         break



import time
progress = 0
while True:
    progress += 10
    print("Hacking", str(progress) + " % ...")
    time.sleep(1)
    if progress == 100:
        print("Hacked!")
        break