#ID 78411394 4 дек 2022, 10:57:32
def nearest_zero(n, data):
    """Функция вычисления ближайщего нуля в последовательности data."""
    count = n
    result = []
    for i in range(n):
        if data[i] == 0:
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
    data = list(map(int, input().strip().split()))
    return n, data


def main():
    n, data = read_input()
    print(" ".join(map(str, nearest_zero(n, data))))


if __name__ == '__main__':
    main()
