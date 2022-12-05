def to_binary(number: int) -> str:
    if number == 0:
        return '0'
    result = []
    while number != 0:
        if number % 2 == 1:
            result.append(1)
        else:
            result.append(0)
        number = number // 2
    return "".join(map(str, result[::-1]))


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
