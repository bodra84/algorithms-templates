from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    zipp = zip(a, b)
    return [x for t in zipp for x in t]


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
# zipper(a, b)
# print(" ".join(map(str, zipper(a, b))))
print(*zipper(a, b))