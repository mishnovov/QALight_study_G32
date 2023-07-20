#Створити просту гру на відгадування чисел, яка дозволяє користувачеві вгадувати випадкове число від 1 до 100.  
#Програма повинна надавати підказки користувачеві після кожного вгадування, 
#вказуючи, чи було його припущення завеликим або замалим,  доки користувач вгадує правильне число.

import random

def play_game():
    random_number = random.randint(1, 100)
    attempts = 0

    print("Вітаю! Спробуйте відгадати число від 1 до 100.")

    while True:
        try:
            guess_num = int(input("Введіть вашу догадку: "))
        except ValueError:
            print("Будь ласка, введіть лише ціле число.")
            continue

        attempts += 1

        if guess_num < random_number:
            print("Запропоноване число замале.")
        elif guess_num > random_number:
            print("Запропоноване число завелике.")
        else:
            print(f"Вітаю! Ви вгадали число {random_number} за {attempts} спроб.")
            break

if __name__ == "__main__":
    play_game()