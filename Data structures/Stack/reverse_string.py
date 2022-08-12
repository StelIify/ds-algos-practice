from Stack.stack import Stack


def reverse_string(stack, string):
    reversed_string = []

    for el in string:
        stack.push(el)

    while not stack.is_empty():
        reversed_string.append(stack.pop())

    return "".join(reversed_string)


stack = Stack()
print(reverse_string(stack, "Hello"))
