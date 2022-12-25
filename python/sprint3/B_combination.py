key = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def combinations(arr):
    res = []
    if len(arr) == 0:
        return ['']
    else:
        word = arr.pop()
        for combination in combinations(arr):
            for char in word:
                res.append(combination + char)
    return res


def read_input():
    number = input()
    return number


def main():
    number = read_input()
    arr =[]
    for x in number:
        arr.append(key[x])
    print(*combinations(arr))


if __name__ == '__main__':
    main()
