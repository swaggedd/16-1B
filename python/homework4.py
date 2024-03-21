# 1
list1 = ["PlayboiCarti", "Gunna", "Porsche911", "BMWm4", "KanyeWest", "21Savage", "Mercedes-Benz", "McLaren", "Osh", "Almaty", "Tashkent", "Bishkek", "Drake", "Rolls-Royce", "Lexus"]
print(list1[2:7])
# 2
numbers = [1, 4, 56, 23, 654, 12, 8, 4, 9, 54,]
print(numbers[::-1])
# 3
a = [1, 3, 4, 5]
b = [4, 5, 6, 7]
a.remove(4)
a.remove(5)
b.remove(4)
b.remove(5)
print(a, b)
# 4
numbers = [3, 4, 56, 23, 654, 12, 8, 4, 9, 54,]
print(min(numbers))
# 5
numbers = [1, 4, 56, 23, 654, 12, 8, 4, 9, 54,]
numbers.clear()
print(numbers)
# 6
numbers = [1, 4, 56, 23, 654, 12, 8, 4, 9, 54,]
print(sum(numbers))
# 7
numbers = [1, 4, 56, 23, 654, 12, 8, 4, 9, 54,]
arif = sum(numbers) / len(numbers)
print(arif)
# 8
playlist = ["n.h.i.e", "mask off", "all girls are the same", "drip too hard", "one call", "p angels", "star shopping", "go crazy", "ball w/o you", "FE!N"]
playlist[3] = playlist[7]
print(playlist)
# 9
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143,
144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158,
159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173,
174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188,
189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203,
204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230,
231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245,
246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275,
276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290,
291, 292, 293, 294, 295, 296, 297, 298, 299, 110, 111, 112, 113, 114, 115,
116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130,
131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,
146, 147, 148, 149, 150, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259,
260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274,
275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289,
290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110]
print(numbers2.count(110))
# 10
it_company = ("Google", "Amazon", "Microsoft")
list_it_company = list(it_company)
print(type(list_it_company))
list_it_company.append("Tesla")
it_company = tuple(list_it_company)
print(type(it_company))
print(it_company)
# 11
print(it_company.index("Amazon"))
# 12
list3 = list_it_company
list3[0] = "Apple"
it_company = tuple(list3)
print(it_company)
# 13
print(it_company[0:3])
# 14
text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
'with', 'our', 'Python', '3', 'overview')
print(text_tuple.count("Python"))
# 15
passwords = []
parol = input("Введите пароль: ")
povtparol = input("Введите пароль еще раз для подтверждения: ")
if parol != povtparol:
    print("Пароли не совпадают!")
elif len(parol) and len(povtparol) < 8:
    print("Короткий пароль!")
elif "123" in parol:
    print("Слишком легкий пароль!")
else:
    print("OK")
    print("Пароль создан!")
    passwords.append(parol)
    print(f'пароли: {passwords}')