from typing import List

def factorize(number: int) -> List[int]:
    i = 1
    a = []
    while i <= number:
        i += 1
        if number % i == 0:
            number = number / i
            a.append(i)
            i = 1
    return a

result = factorize(int(input()))
print(" ".join(map(str, result)))
