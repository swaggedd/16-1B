# 1
password = "123Rus"
passw = input("Введите пароль: ")
if passw == password:
    print("Password is correct")
else:
    print("Password is incorrect")
# 2
temperature = int(input("Введите температуру за окном: "))
if temperature < -30:
    print("Там так холодно, лучше дома сиди!")
elif -30 <= temperature < 0:
    print("Холодновато. Оденься потеплее!")
elif 0 <= temperature < 15:
    print("Прохладно. Куртку накинь!")
elif 15 <= temperature < 30:
    print("Тепло. Иди погуляй в парке!")
elif 30 <= temperature <= 50:
    print("Ого, как жарко!")
elif temperature > 50:
    print("Там такая жара, лучше сиди дома!")
else:
    print("Ошибка!")
# 3
hour = int(input("Введите текущий час (от 0 до 23): "))
if 0 <= hour < 6:
    print("Ночь (0 - 5 часов)")
elif 6 <= hour < 12:
    print("Утро (6 - 11 часов)")
elif 12 <= hour < 18:
    print("День (12 - 17 часов)")
elif 18 <= hour <= 23:
    print("Вечер (18 - 23 часов)")
else:
    print("Ошибка!")
# 4 (доп задача)
grade = int(input("Введите оценку студента (от 0 до 100): "))
if grade >= 90:
    print("Отлично")
elif 80 <= grade < 90:
    print("Хорошо")
elif 70 <= grade < 80:
    print("Удовлетворительно")
elif 60 <= grade < 70:
    print("Неудовлетворительно")
else:
    print("Студент должен пересдать экзамен")
