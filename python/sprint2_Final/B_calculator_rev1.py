# 79871659 21 дек 2022, 22:47:46
operation = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x // y
             }


class Stack:
    """Класс стека."""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Метод добавляет элемент на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Метод возвращает элемент с вершины стека и удаляет его."""
        return self.items.pop()

    def top(self):
        """Метод возвращает элемент с вершины стека, не удаляя его."""
        return self.items[-1]

    def size(self):
        """Метод возвращает размер стека."""
        return len(self.items)


def read_input():
    """Функция ввода исходных данных."""
    data = input().split()
    return data


def main():
    data = read_input()
    notation = Stack()
    while data:
        item = data.pop(0)
        if item not in operation:
            notation.push(int(item))
        else:
            y = notation.pop()
            x = notation.pop()
            result = operation[item](x, y)
            notation.push(result)
    result = notation.top()
    print(result)


if __name__ == '__main__':
    main()
