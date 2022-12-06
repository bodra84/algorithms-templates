def is_power_of_four(number: int) -> bool:
    if number in (1, 4):
        return True
    while number > 0:
        c = number // 4
        o = number % 4
        if 2 < c <= 4 and o == 0:
            return True
        elif 0 < o < 4:
            return False
        number = c


print(is_power_of_four(int(input())))
