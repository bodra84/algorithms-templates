# 79870321 21 дек 2022, 22:13:31
class DequeIsFull(Exception):
    """Ошибка при добавлении элемента в переполенный дек."""
    pass


class DequeIsEmpty(Exception):
    """Ошибка при получении элемента из пустого дека."""
    pass


class Deque:
    """Класс Дек."""
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        """Метод проверяет пуста ли очередь."""
        return self.size == 0

    def push_back(self, value):
        """Метод добавляет элемент в конец дека."""
        if self.size != self.max:
            while self.queue[self.tail]:
                self.tail = (self.tail + 1) % self.max
            self.queue[self.tail] = value
            self.size += 1
        else:
            raise DequeIsFull()

    def push_front(self, value):
        """Метод добавляет элемент в начало дека."""
        if self.size != self.max:
            while self.queue[self.head]:
                self.head = (self.head - 1) % self.max
            self.queue[self.head] = value
            self.size += 1
        else:
            raise DequeIsFull()

    def pop_back(self):
        """Метод возвращает последний элемент дека и удаляет его."""
        if self.is_empty():
            raise DequeIsEmpty()
        value = self.queue[self.tail]
        self.queue[self.tail] = None
        if self.size > 1:
            self.tail = (self.tail-1) % self.max
        self.size -= 1
        return value

    def pop_front(self):
        """Метод возвращает первый элемент дека и удаляет его."""
        if self.is_empty():
            raise DequeIsEmpty()
        value = self.queue[self.head]
        self.queue[self.head] = None
        if self.size > 1:
            self.head = (self.head + 1) % self.max
        self.size -= 1
        return value


def read_input():
    """Функция ввода исходных данных."""
    n = int(input())
    size = int(input())
    data = ([input().split() for _ in range(n)])
    return size, data


stack_methods = {'push_back': Deque.push_back, 'pop_back': Deque.pop_back,
                 'push_front': Deque.push_front, 'pop_front': Deque.pop_front}


def main():
    max_size, data = read_input()
    q = Deque(max_size)
    for command, *args in data:
        try:
            result = getattr(q, command)(*args)
            if result:
                print(result)
        except AttributeError:
            print("Ошибка команды!")
        except DequeIsFull:
            print("error")
        except DequeIsEmpty:
            print("error")


if __name__ == '__main__':
    main()
