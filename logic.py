from random import randint
from decouple import config


def load_settings():
    min_num = config("MIN_NUM", cast=int)
    max_num = config("MAX_NUM", cast=int)
    attempts = config("ATTEMPTS", cast=int)
    initial_capital = config("INITIAL_CAPITAL", cast=int)
    return min_num, max_num, attempts, initial_capital
if __name__ == '__main__':
    print(load_settings())

def play_game():
    min_num, max_num, attempts, initial_capital = load_settings()
    sekret_num = randint(min_num, max_num)
    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Диапазон чисел: от {min_num} до {max_num}.")
    print(f"У вас {attempts} попыток и стартовый баланс: {initial_capital}.")

    while attempts > 0:
        try:
            bet = int(input(f'Сделайте ставку (доступно {initial_capital}): '))
            if bet > initial_capital or bet <= 0:
                print("Неверная ставка. Попробуйте снова.")
                continue
            guess = int(input(f"Угадайте число (попыток осталось: {attempts}): "))

            if guess == sekret_num:
                initial_capital += bet
                print(f"Поздравляем! Вы угадали число "
                      f"{sekret_num}. Ваш баланс: {initial_capital}.")
                break
            else:
                initial_capital -= bet
                attempts -= 1
                if attempts > 0:
                    print(f"Неправильно! Баланс: {initial_capital}."
                          f" Осталось попыток: {attempts}.")
                else:
                    print(f"Вы проиграли! Число было: {sekret_num}."
                          f" Баланс: {initial_capital}.")
        except ValueError:
            print("Пожалуйста, введите числовое значение.")


    print("Спасибо за игру!")

if __name__ == '__main__':
    print(play_game())
