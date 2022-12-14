class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return print('error')

    def get_max(self):
        if self.items:
            return print(max(self.items))
        return print('None')


def read_input():
    """Функция ввода исходных данных."""
    data = []
    n = int(input())
    data = ([input().split() for _ in range(n)])
    return data


stack_methods = {'push': StackMax.push, 'pop': StackMax.pop,
                 'get_max': StackMax.get_max}


def main():
    comands = read_input()
    stack = StackMax()
    for comand in comands:
        if len(comand) > 1:
            stack_methods[comand[0]](stack, int(comand[1]))
        else:
            stack_methods[comand[0]](stack)


if __name__ == '__main__':
    main()
