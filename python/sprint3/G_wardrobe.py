def wardrobe(arr):
    colors = {str(i): 0 for i in range(0, 3)}
    for char in arr:
        if char in colors:
            colors[char] += 1
    for key, color in colors.items():
        print((key+' ')*color, end='')


def read_input():
    """Функция ввода исходных данных."""
    _ = int(input())
    data = input().split()
    return data


def main():
    data = read_input()
    wardrobe(data)


if __name__ == '__main__':
    main()
