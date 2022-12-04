#ID 78644233 4 дек 2022, 16:50:40
def sleight_hand(k, data):
    """
    Функция вычисления количества баллов, заработанных при оновременном нажатии
    на 2*к клавиш в поле исходных данных data.
    """
    keys = {str(i): 0 for i in range(1, 10)}
    result = 0
    for char in data:
        if char in keys:
            keys[char] += 1
    for value in keys.values():
        if value <= (k + k) and value != 0:
            result += 1
    return result


def read_input():
    """Функция ввода исходных данных."""
    k = int(input())
    data = ''.join([input().strip() for _ in range(4)])
    return k, data


def main():
    k, data = read_input()
    print(sleight_hand(k, data))


if __name__ == '__main__':
    main()
