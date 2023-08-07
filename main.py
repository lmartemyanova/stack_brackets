from Stack import Stack


def check_brackets(data: str):
    brackets_balanced = {'(': ')', '[': ']', '{': '}'}
    stack = Stack()
    for elem in data:
        if elem in brackets_balanced.keys():
            stack.push(elem)
        else:
            if stack.is_empty():
                return 'Несбалансированно'
            elif elem in brackets_balanced.values() and brackets_balanced[stack.peek()] == elem:
                stack.pop()
            else:
                return 'Несбалансированно'
    if stack.is_empty():
        return 'Сбалансированно'
    return 'Несбалансированно'


if __name__ == '__main__':
    while True:
        data = input('Введите последовательность скобок: ')
        print(check_brackets(data))