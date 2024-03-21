# 1) Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}.
# Объедините их в один при помощи встроенных функций языка Python. Подсказка:
# метод update()

dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)

# 2) Дан словарь с числовыми значениями. numbers = {‘num_1’ : 1, ‘num_2’ : 2, ‘num_3’ :
# 3, ‘num_100’ : 100} Необходимо умножить все числовые значения словаря на 5 и
# вывести в терминал.

numbers = {"num_1" : 1, "num_2" : 2, "num_3" : 3, "num_100" : 100}
for i in numbers.values():
    i = i * 5
    print(i)


# 3) Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Умножьте его age на 2 раза

student1 = {"name" : "Askhat", "age" : 17}
mul = student1["age"] * 2
print(mul)


# 4) Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17, ‘color’ : ‘White’}. Обновите age в 16

student2 = {"name" : "Askhat", "age" : 17, "color" : "White"}
student2["age"] = 16
print(student2)


# 5) Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Удалите ключ и значение age

student3 = {"name" : "Askhat", "age" : 17}
student3.pop("age")
print(student3)

# 6) Есть словарь student = {‘name’ : ‘Askhat’}. Добавьте новый ключ(address) и
# значение(Западный Анар)

student4 = {'name': 'Askhat'}
student4.setdefault("address", "Western Anar")
print(student4)

# ДОП ЗАДАНИЕ:
# 7) Напишите функцию -- чат-бот с бесконечным циклом, который
# a. Всегда отвечает “Конечно!” на любой вопрос
# b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
# c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же духе!” Если
# вызвал функцию, но ничего не передал.
# d. В любых других случаях, отвечает “ну и что”

def bot():
    while True:
        a = input("Напиши что-нибудь или задай вопрос: ")
        if a.endswith("?"):
            print("Конечно!")
        elif not a:
            print("Как классно когда ты молчишь. Продолжай в том же духе!")
        elif a.endswith("!") and a.upper():
            print("Успокойся")
        else:
            print("Ну и что")
# bot()
# 8) Напишите функцию, которая принимает фразу, и возвращает его сокращенную
# форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest -- FYI и
# т.п.

def frase():
    frs = input("Введите фразу для ее сокращения: ").split()
    sokr = ''
    for i in frs:
        sokr += i[0].upper()
    print(sokr)
# frase()
    

# 9) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной
# фразе было использовано.
# Например: “Money, money, money, it’s always sunny, in the richmen’s world”. money: 3, it’s:
# 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1.

def wordscount():
    text = input("Напишите какой-нибудь текст, предложение: ").split()
    count = {}
    for word in text:
        count[word] = count.get(word, 0) + 1
    print(count)
# wordscount()

# 10) Напишите функцию, которая принимает слово и возвращает True, если слово
# изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False.

def isogram(word):
    word = word.lower()
    count = {}
    for letter in word:
        if letter in count:
            return False
        else:
            count[letter] = 1
    return True
word = input("Введите слово: ")
if isogram(word):
    print("Isogram")
else:
    print("Not isogram")


# 11) Напишите функцию где мы передаем через аргументы число n, надо вывести
# сумму чисел n и “перевёрнутого” n, например: n = 27, тогда перевёрнутое n это 72

def number(n):
    reversn = str(n)[::-1]
    revint = int(reversn)
    summ = n + revint
    return summ

n = int(input("Введите число: "))
result = number(n)
print(f"Сумма n и его перевернутого варианта: {result}")
