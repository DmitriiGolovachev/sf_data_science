"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число от 0 до 100

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    number_list = [i for i in range(0, 101)]  # возможные значения number

    def binary_search(number: int, low: int = 1, high: int = 100) -> int:
        """Функция бинарного поиска загаданного числа

        Args:
            number (int): загаданное число
            low (int, optional): нижняя граница поиска. Defaults to 1.
            high (int, optional): верхняя граница посика. Defaults to 101.

        Returns:
            int: число попыток
        """
        nonlocal count
        nonlocal number_list

        if low <= high:
            mid = int((low + high) / 2)  # середина диапазона поиска
            if number_list[mid] > number:
                count += 1
                return binary_search(number, low, mid - 1)
            elif number_list[mid] < number:
                count += 1
                return binary_search(number, mid + 1, high)
            else:
                return count  # индекс загаданного элемента
        else:
            return -1  # загаданного элемента нет в списке number_list

    return binary_search(number)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов
    угадывает наш алгоритм.

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    # загадали список чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


if __name__ == '__main__':
    score_game(random_predict)
