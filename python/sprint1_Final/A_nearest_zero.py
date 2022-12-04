#ID 78639100 4 дек 2022, 16:36:55
def nearest_zero(n, data):
    """Функция вычисления ближайщего нуля в последовательности data."""
    count = n
    result = []
    for num in data:
        if num == 0:
            result.append(0)
            count = 1
        else:
            result.append(count)
            count += 1
    count = n
    for i in range(n-1, -1, -1):
        if result[i] == 0:
            count = 1
        else:
            if result[i] > count:
                result[i] = count
            count += 1
    return result


def read_input():
    """Функция ввода исходных данных."""
    n = int(input())
    data = [int(i) for i in input().split()]
    return n, data


def main():
    n, data = read_input()
    print(*nearest_zero(n, data))


if __name__ == '__main__':
    main()
