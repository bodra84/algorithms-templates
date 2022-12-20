# 79812130 20 дек 2022, 20:59:39
data = input().split()
operation = {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: x // y
             }
stack = []
while data:
    item = data.pop(0)
    if item not in operation:
        stack.append(int(item))
    else:
        y = stack.pop()
        x = stack.pop()
        result = operation[item](x, y)
        stack.append(result)
result = stack.pop()
print(result)
