def correct(prefix):
    for _ in range(len(prefix)//2):
        prefix = prefix.replace('()', '')
    return len(prefix) == 0


def gen_binary(n, prefix=''):
    if n == 0 and correct(prefix):
        print(prefix)
    elif n == 0:
        pass
    else:
        gen_binary(n - 1, prefix + '(')
        gen_binary(n - 1, prefix + ')')


def read_input():
    n = int(input())
    return n


def main():
    n = read_input()
    gen_binary(2*n)


if __name__ == '__main__':
    main()

