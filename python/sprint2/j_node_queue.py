class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def get(node):
    if not node.next:
        print('error')
    else:
        next_node = node.next
        x = next_node.value
        node.next = next_node.next
        print(x)


def put(node, x):
    if not node.next:
        node.next = Node(x)
    else:
        while node.next:
            node = node.next
        node.next = Node(x)


def size(node):
    idx = 0
    while node.next:
        idx += 1
        node = node.next
    print(idx)


def pechat(node):
    print(node.value, node.next)


def read_input():
    """Функция ввода исходных данных."""
    data = []
    n = int(input())
    data = ([input().split() for _ in range(n)])
    return data


stack_methods = {'size': size, 'put': put, 'get': get, 'pechat': pechat}


def main():
    comands = read_input()
    node = Node(0)
    for comand in comands:
        if len(comand) > 1:
            stack_methods[comand[0]](node, int(comand[1]))
        else:
            stack_methods[comand[0]](node)


if __name__ == '__main__':
    main()
