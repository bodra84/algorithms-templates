#ID 78101258 3 дек 2022, 14:33:25
def get_house(n, street):
    count = n
    result = []
    for i in range(n):
        if street[i] == 0:
            result.append(0)
            count = 1
        else:
            result.append(count)
            count += 1
    count = n
    for i in range(n-1, -1, -1):
        if result[i] == 0:
            count = 1
        else:
            if result[i] > count:
                result[i] = count
            count += 1
    return result

def read_input():
    n = int(input())
    street = list(map(int, input().strip().split()))
    return n, street

n, street = read_input()
print(" ".join(map(str, get_house(n, street))))
