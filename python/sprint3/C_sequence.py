def sequence(s, t):
    if len(s) > len(t):
        return False
    left = 0
    for i in s:
        try:
            right = t.index(i, left)
        except ValueError:
            return False
        left = right + 1
    return True


def read_input():
    """Функция ввода исходных данных."""
    s = list(input())
    t = list(input())
    return s, t


def main():
    s, t = read_input()
    print(sequence(s, t))


if __name__ == '__main__':
    main()
