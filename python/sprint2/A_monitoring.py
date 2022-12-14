def read_input():
    """Функция ввода исходных данных."""
    data = []
    x = int(input())
    y = int(input())
    data = ([input().split() for _ in range(x)])
    return x, y, data

def main():
    x, y, data = read_input()
    for i in range(y):
        char = str()
        char = ' '.join([data[j][i] for j in range(x)])
        print(char)


if __name__ == '__main__':
    main()