# from typing import List
#
#
# def get_weather_randomness(temperatures: List[int]) -> int:
#     temperatures = ([min(temperatures) - 1]
#                     + temperatures
#                     + [min(temperatures) - 1])
#     w_ch = len([n for n in range(1, len(temperatures)) if
#                 temperatures[n - 1] < temperatures[n] > temperatures[n + 1]])
#     return w_ch
#
#
# def read_input() -> List[int]:
#     n = int(input())
#     temperatures = list(map(int, input().strip().split()))
#     return temperatures
#
#
# temperatures = read_input()
# print(get_weather_randomness(temperatures))
##############################################################################
from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    count = 0
    last_idx = len(temperatures) - 1

    for i, value in enumerate(temperatures):
        if i == 0:
            continue
        if i != last_idx:
            if temperatures[i - 1] < value > temperatures[i + 1]:
                count += 1
        else:
            if temperatures[i - 1] < value:
                count += 1
    return count


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))

import sys

##############################################################################
def main():
    n = int(input())
    if n == 1:
        return print(n)

    line = list(map(int, sys.stdin.readline().rstrip().split()))
    result = 0
    line.insert(0, -274)
    line.append(-274)
    i=1
    while i < n + 1:
        if line[i - 1] < line[i] > line[i + 1]:
            result += 1
        i+=1
    return print(result)


if __name__ == '__main__':
    main()