# file_write = open("test", "w")
# file_write.write("N- u think im dumb enough to give ur ahh a louded gun after the shi- u just pulled? im the smart one")

# while True:
#     for i in range(1,2):
#         hacking = open(f'haha{i}.txt', "w")
#         hacking.write("Вас взломали")


# user = input("Введите имя: ")
# age = int(input("Введите возраст: "))
# number = int(input("Введите телефонный номер: "))
# filew = open("users.txt", "w")
# filew.write(f'Name: {user} \nAge: {age} \nTelephone number: {number}')

# read = open("geeks.txt", "r")
# result = read.read()
# print(result)

# test = open("geeks.txt", "r")
# result = test.read()
# print(result)

# users = ["Besdultan", "Muha", "Islam", "Anton", "Musu"]
# with open("userlist.txt", "w") as write_text:
#     write_text.write(f'Users: {users}')

# with open("geeks.txt", "r") as read_file:
#     result = read_file.read()
#     print(result)


# lambda - анонимная функция

# summ = lambda num1, num2: num1*num2
# print(summ(5,3))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[::-1])
# reverse = lambda x: x[::-1]
# print(reverse(numbers))

users = ["Mergul", "Beksultan", "Islam", "Vlad"]
# result = list(map(lambda name: f'{name} - {len(name)}', users))
# print(result)

result2 = list(map(lambda x: x[0], users))
print(result2)

result3 = list(map(lambda x: x.upper(), users))
print(result3)