import sys

def get_house(n, street):
    empty = []
    occupied = []
    i = 0
    while i < n:
        if street[i] == 0:
            empty.append(i)
        else:
            occupied.append(i)
        i += 1
    h = 0
    while h < len(occupied):
        result = []
        z = 0
        for z in empty:
            result.append(abs(h-z))

        street[h] = min(result)
        h += 1
    return street


def main():
    n = int(input())
    street = list(map(int, sys.stdin.readline().rstrip().split()))
    print(" ".join(map(str, get_house(n, street))))


if __name__ == '__main__':
    main()
