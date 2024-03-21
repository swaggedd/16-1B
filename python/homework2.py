# 1
change = input("Введите что нибудь: ")
modd = change.replace('a', 'o')
print("Результат:", modd)
# 2
str1 = input("Введите строку: ")
print(str1+str1)
# 3
str2 = input("Введите что-то:")
print(str2[0])
# 4
str2 = input("Введите что-то:")
print(str2[-1])
# 5
str3 = input("Введите строку: ")
repl = str3.replace(" ", "-")
print(repl)
# 6
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
print("Ваши инициалы: ", name[0].upper(), surname[0].upper())
# 7
str4 = input("Введите строку: ")
print(f'Количество: {str4.count("a")}')
# 8
str5 = input("Введите строку:").title()
print(str5)
# 9
str6 = input("Введите строку: ")
print(f'длина: {len(str6)}')