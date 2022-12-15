def correct_parentheses(s):
    dl = len(s)
    if dl == 0:
        return True
    n = dl // 2
    for i in range(n):
        s = s.replace('()', '', n)
        s = s.replace('[]', '', n)
        s = s.replace('{}', '', n)
        if len(s) == 0:
            return True
    return False


def main() -> None:
    arr = input()
    print(correct_parentheses(arr))


if __name__ == '__main__':
    main()
