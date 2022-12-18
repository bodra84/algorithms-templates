class Deque:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.size != self.max:
            while self.queue[self.tail]:
                self.tail = (self.tail + 1) % self.max
            self.queue[self.tail] = x
            self.size += 1
        else:
            return print('error')

    def push_front(self, x):
        if self.size != self.max:
            while self.queue[self.head]:
                self.head = (self.head - 1) % self.max
            self.queue[self.head] = x
            self.size += 1
        else:
            return print('error')

    def pop_back(self):
        if self.is_empty():
            return print('error')
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        if self.size > 1:
            self.tail = (self.tail-1) % self.max
        self.size -= 1
        return print(x)

    def pop_front(self):
        if self.is_empty():
            return print('error')
        x = self.queue[self.head]
        self.queue[self.head] = None
        if self.size > 1:
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


stack_methods = {'push_back': Deque.push_back, 'pop_back': Deque.pop_back,
                 'push_front': Deque.push_front, 'pop_front': Deque.pop_front}


def main():
    max_size, comands = read_input()
    q = Deque(max_size)
    for comand in comands:
        if len(comand) > 1:
            stack_methods[comand[0]](q, int(comand[1]))
        else:
            stack_methods[comand[0]](q)


if __name__ == '__main__':
    main()
