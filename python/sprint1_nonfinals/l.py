from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    a = sorted(shorter)
    b = sorted(longer)
    if len(b) > len(a):
        a, b = b, a
    count_a = 0
    count_b = 0
    for char in a:
        count_a = a.count(char)
        count_b = b.count(char)
        if (count_a == 0 or count_b == 0 or count_a > count_b
                or count_a < count_b):
            return char


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
