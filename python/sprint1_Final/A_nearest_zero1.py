def get_house(n, street):
    l = [i for i, v in enumerate(street) if v == 0]
    m_l = []
    for i, ls in enumerate(street):
        m = n
        for j in l:
            if m > abs(i - j):
                m = abs(i - j)
        m_l.append(m)
    return m_l


def read_input():
    n = int(input())
    street = list(map(int, input().strip().split()))
    return n, street


n, street = read_input()
print(" ".join(map(str, get_house(n, street))))


