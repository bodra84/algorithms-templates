import re


def is_palindrome(line: str) -> bool:
    line = line.lower()
    line = re.split(r'\W+', line)
    line = "".join(map(str, line))
    line2 = line[::-1]
    if line == line2:
        return True
    return False


print(is_palindrome(input().strip()))
