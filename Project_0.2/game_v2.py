"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    a = 1 # изменяемая нижняя граница рассматриваемого отрезка 
    b = 100 # изменяемая нижняя граница рассматриваемого отрезка 
    mean_number = int(np.median([a, b])) # медиана

    while True:
        count += 1
        if number == mean_number:
            break  # выход из цикла если угадали
        elif number > mean_number:
            a = mean_number # изменяем нижнюю границу
            mean_number = mean_number + int(np.median([mean_number, b])) # находим новую медиану
        elif number < mean_number:
            b = mean_number # изменяем верхнюю границу
            mean_number = int(np.median([a, mean_number])) # находим новую медиану
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
