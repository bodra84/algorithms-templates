# ID 80272195 4 янв 2023, 13:44:47
from random import randint
from dataclasses import dataclass, field


@dataclass(order=True)
class Player:
    """Класс участника соревнования."""
    solved: int = field(compare=False)
    score_to_compare: int = field(init=False, repr=False)
    penalty: int
    login: str

    def __post_init__(self):
        self.score_to_compare = self.solved * (-1)

    def __str__(self):
        return self.login


def partition(array, pivot, left, right):
    """
    Функция делит массив на две части относительно опорного элемента
    (pivot). Слева - элементы меньше, справа - больше.
    """
    while left <= right:
        while array[left] < pivot:
            left += 1
        while pivot < array[right]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left, right


def quick_sort(array, first=0, last=None):
    """Функция быстрой сортировки. Опорный элемент рандомный (pivot)."""
    if last is None:
        last = len(array) - 1
    if first >= last:
        return
    pivot = array[randint(first, last)]
    left, right = partition(array, pivot, first, last)
    quick_sort(array, first, right)
    quick_sort(array, left, last)


def read_input():
    """Функция ввода исходных данных."""
    n = int(input())
    players = []
    for _ in range(n):
        data = input().split()
        try:
            player = Player(login=data[0],
                            solved=int(data[1]),
                            penalty=int(data[2]),
                            )
            players.append(player)
        except ValueError:
            pass
    return players


def main():
    players = read_input()
    quick_sort(players)
    [print(player) for player in players]


if __name__ == '__main__':
    main()
