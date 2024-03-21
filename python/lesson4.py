# names = ["Nurbolot", "Timur", "Janush", "Islam", "Syimyk"]
# print(names)
# example_list = [10, 1.0, True, "Geeks"]
# print(example_list)


# it_companies = ["Geeks", "MadDevs", "Codex", "Meta", "Google"]
# print(it_companies)
# print(it_companies[0])
# print(it_companies[3])
# print(it_companies[3][2])
# print(it_companies[1:4:2])
# print(it_companies[::-1])
# it_companies.append("Tesla")
# print(it_companies)
# it_companies.remove("MadDevs")
# print(it_companies)
# it_companies[2] = "Facebook"
# print(it_companies)
# it_companies.insert(0, "Prolab")
# print(it_companies)
# it_companies.pop(3)
# print(it_companies)
numbers = [1, 100, 44, 2, 56, 78, 12, 505]
numbers.sort()
print(numbers)


cars = ["BMW", "Mercedes-Benz", "Tesla", "Zeekr", "Audi"]
print(cars)
print(cars.index("Zeekr"))  
cars.clear()
print(cars)


# Кортежи - Tuple

# colors = ("White", "Black", "Red")
# print(colors)
# print(colors.count("Black"))
# print(colors[0])
# print(colors[1:3])
# print(colors[::-1])

# data = ("Geeks",)
# print(data)
# print(type(data))

# pg_languages = ("Python", "JavaScript", "C#")
# print(pg_languages)

# list_pg_languages = list(pg_languages)
# print(list_pg_languages)
# print(type(list_pg_languages))

# list_pg_languages.append('Java')
# list_pg_languages.append('C++')
# print(list_pg_languages)
# pg_languages = tuple(list_pg_languages)
# print(pg_languages)

contacts = ["Kurmanbek", "Aziz", "Timur", "Esenbek"]
find_contact = input("Введите имя: ").title()
if find_contact in contacts:
    print(f'контакт {find_contact} найден')
else:
    print(f'контакт {find_contact} не найден')