import re


def get_longest_word(line: str) -> str:
    result = ()
    line = re.findall(r'\S+', line)
    maxlen = max(len(word) for word in line)
    for word in line:
        if len(word) == maxlen:
            result = word
            break
    return result


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
