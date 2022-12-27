def buble_sort(arr, n):
    f1 = True
    for j in range(0, n - 1):
        f2 = False
        for i in range(0, n - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                f2 = True
                f1 = False

        if f1:
            print(*arr)
            break

        if f2:
            print(*arr)
        else:
            break


def read_input():
    n = int(input())
    data = [int(x) for x in input().split()]
    return n, data


def main():
    n, arr = read_input()
    buble_sort(arr, n)


if __name__ == '__main__':
    main()
