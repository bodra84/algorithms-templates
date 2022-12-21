def get_house(n, street):
    empty = []
    occupied = []
    for i in range(n):
        if street[i] == 0:
            empty.append(i)
        else:
            occupied.append(i)
    for h in occupied:
        result = []
        for z in empty:
            result.append(abs(h-z))

        street[h] = min(result)
    return street


def read_input():
    """Функция ввода исходных данных."""
    n = int(input())
    street = list(map(int, input().strip().split()))
    return n, street


def main():
    n, street = read_input()
    print(" ".join(map(str, get_house(n, street))))


if __name__ == '__main__':
    main()
