import random 


def computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)

def win(player_choice, comp_choice):
    if player_choice == comp_choice:
        print("Ничья")
    elif player_choice == "камень" and comp_choice == "ножницы" or player_choice == "ножницы" and comp_choice == "бумага" or player_choice == "бумага" and comp_choice == "камень":
        print("Ты выиграл")
    else:
        print("Ты проиграл")
        