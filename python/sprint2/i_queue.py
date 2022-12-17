class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, x):
        if self.size != self.max:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max
            self.size += 1
        else:
            return print('error')

    def peek(self):
        if self.is_empty():
            return print('None')
        return print(self.queue[self.head])

    def size(self):
        return print(self.size)

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty():
            return print('None')
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max
        self.size -= 1
        return print(x)


def read_input():
    """Функция ввода исходных данных."""
    data = []
    n = int(input())
    size = int(input())
    data = ([input().split() for _ in range(n)])
    return size, data


stack_methods = {'push': MyQueueSized.push, 'pop': MyQueueSized.pop,
                 'size': MyQueueSized.size, 'peek': MyQueueSized.peek}


def main():
    max_size, comands = read_input()
    q = MyQueueSized(max_size)
    for comand in comands:
        if len(comand) > 1:
            stack_methods[comand[0]](q, int(comand[1]))
        else:
            stack_methods[comand[0]](q)


if __name__ == '__main__':
    main()
