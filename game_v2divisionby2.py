"""Игра угадай число
Компьютер сам загадывает, а программа угадывает число
"""

import numpy as np


def predict(number: int = 1) -> int:
    """Угадываем число, постоянно сокращая в 2 раза диапазон доступных решений

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    val_max = 101
    val_min = 0
    predict_number = (val_max-val_min) // 2  # Предполагаемое число, начинаем с середины диапазона
    count = 1  # Принимаю за единицу, потому что по сути, определение середины диапазона уже является первой попыткой
    
    while True:
        count += 1
        if number > predict_number:
            val_min = predict_number
            predict_number = (val_max-val_min) // 2 + val_min
        elif number < predict_number:
            val_max = predict_number
            predict_number = (val_max-val_min) // 2 + val_min
        elif number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict)
