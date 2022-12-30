def merge(s):
    for i in range(len(s) - 1):
        if s[i + 1][0] <= s[i][1]:
            s[i + 1][0] = s[i][0]
            if s[i][1] > s[i + 1][1]:
                s[i + 1][1] = s[i][1]
            s[i] = []
    for j in range(len(s)):
        if s[j]:
            print(*s[j])


def read_input():
    """Функция ввода исходных данных."""
    n = int(input())
    data = []
    for _ in range(n):
        seq = [int(x) for x in input().split()]
        data.append(seq)
    data.sort()
    return data


def main():
    data = read_input()
    merge(data)


if __name__ == '__main__':
    main()
