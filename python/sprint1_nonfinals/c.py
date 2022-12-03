from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    rows, cols = range(len(matrix)), range(len(matrix[0]))
    offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    result = []
    for dy, dx in offsets:
        ny, nx = row + dy, col + dx
        if ny in rows and nx in cols:
            result.append(matrix[ny][nx])
    result.sort()
    return result


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
