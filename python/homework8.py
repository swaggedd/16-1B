# 1) Напишите функцию, которая принимает список, из списка выдает случайное значение из списка и записывает результат в txt файл. 
# Список language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"] 

import random
def filew(lst, filename):
    random_val = random.choice(lst)
    with open(filename, "w") as h8:
        h8.write(random_val)

language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"] 
# filew(language, "h8")


# 2) У нас есть переменная text которая, хранит в себе текст: 
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularized in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. 
# Откройте файл text.txt и запишите текст в файл 2 способами

file_write = open("lorem.txt", "w")
file_write.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularized in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

text2 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularized in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
with open("file_write.txt", "w") as lorem2:
    lorem2.write(text2)

# 3) Написать программу, которая откроет созданный в задаче 2 файл text.txt, скопирует весь текст и запишет его в новый файл wikipedia.txt .

def copy_file(source, copy):
    with open(source, "r") as read_file:
        text = read_file.read()

    with open(copy, "w") as copy_text:
        copy_text.write(text) 
source = "file_write.txt"
copy = "copy_text.txt"
# copy_file(source, copy)


# ДОП ЗАДАЧА:

# 4) Напишите программу, которая открывает файл 'data.txt' записывает туда 30 случайных чисел и затем считывает все числа из файла, находит и выводит максимальное число.

with open("data.txt", "w") as numbers:
    for i in range(30):
        numbers.write(str(random.randint(1, 100)) + "\n")
with open("data.txt", "r") as count:
    numbs = [int(line.strip()) for line in count]
if numbers:
    print(f'Максимальное число {max(numbs)}')
else:
    print("Ошибка")


# 5) Создайте функцию, которая принимает на вход список слов и возвращает список слов, начинающихся с определенной буквы, например, 'а'.

def words(wordlst, letter):
    selected_words = []
    for word in wordlst:
        if word.startswith(letter):
            selected_words.append(word)
    return selected_words
wordlst = ["Apple", "Banana", "Apricot", "Avocado", "Berry"]
letter = 'A'
slwords = words(wordlst, letter)
print(f"Слова, начинающиеся с буквы {letter}: {slwords}")


# 6) Напишите программу, которая считывает файл 'input.txt' и создает новый файл 'output.txt', в котором записаны все слова из 'input.txt', начинающиеся с гласной буквы.

inputwords = ["apple", "banana", "cat", "dog", "elephant", "fish", "grape", "horse", "igloo", "jelly", "kangaroo", "lion", "monkey"]
glas_letters = ['e', 'u', 'i', 'o', 'a']
glas_words = []
with open("input.txt", "w") as input1:
    input1.write(str(inputwords))
with open("input.txt", "r") as output:
    check = output.read()
for i in inputwords:
    if i[0] in glas_letters:
        glas_words.append(i)
with open("output.txt", "w") as output:
    writewords = output.write(str(glas_words))


# 7) Создайте lambda-функцию, которая принимает на вход список чисел и возвращает список квадратов этих чисел.

nums = [3, 6, 23, 65, 33, 88, 876, 999]
result = list(map(lambda x: x**2, nums))
print(result)


# 8) Напишите программу, которая открывает файл 'data.txt', считывает числа из файла, вычисляет и выводит их среднее арифметическое.

with open("data.txt", "r") as square:
    nums = [int(line.strip()) for line in square]
if nums:
    result2 = sum(nums) / len(nums)
    print(result2)
else:
    print("Ошибка")