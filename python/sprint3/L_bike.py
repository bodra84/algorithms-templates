def byebike(day, sum, fday, lday):
    if lday <= fday or int(day[lday - 1]) < sum:
        return -1
    mid = (fday + lday) // 2
    if (int(day[mid]) >= sum and mid == fday) or (
            int(day[mid]) >= sum > int(day[mid-1])):
        return mid + 1
    elif sum > int(day[mid]):
        return byebike(day, sum, mid+1, lday)
    else:
        return byebike(day, sum, fday, mid)


def read_input():
    n = int(input())
    data = input().split()
    summa = int(input())
    return n, data, summa


def main():
    n, data, summa = read_input()
    days = (byebike(data, summa, 0, n), byebike(data, summa * 2, 0, n))
    print(*days)


if __name__ == '__main__':
    main()
