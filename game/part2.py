from part1 import computer_choice, win

def play_game():
    print("Игра камень, ножницы, бумага.")

    while True:
        player_choice = input("Введите ваш выбор(камень, ножницы или бумага). Для выхода напишите 'выход': ").lower().replace(" ", "")

        if player_choice == "выход":
            print("Спасибо за игру")
            break
        elif player_choice not in ["ножницы", "камень", "бумага"]:
            print("Неверный выбор")
            break
        comput_choice = computer_choice()

        print(f'Компьютер выбрал: {comput_choice}')

        win(player_choice, comput_choice)


play_game()