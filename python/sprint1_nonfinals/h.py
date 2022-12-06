from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    width = max(len(first_number), len(second_number))
    f = first_number.zfill(width)
    s = second_number.zfill(width)
    result = []
    r = 0
    for i in range(width-1, -1, -1):
        t = int(f[i]) + int(s[i]) + r
        if t > 1:
            t -= 2
            r = 1
        else:
            r = 0
        result.append('1' if t else '0')
    if r == 1:
        result.append('1')
    result.reverse()
    return "".join(result)


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()

print(get_sum(first_number, second_number))
