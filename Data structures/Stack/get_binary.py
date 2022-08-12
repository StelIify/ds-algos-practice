from Stack.stack import Stack


def get_binary(stack, number):
    binary_number = []

    while True:
        remainder = number % 2
        number = number // 2
        stack.push(remainder)
        if number == 0:
            break

    while not stack.is_empty():
        binary_number.append(stack.pop())

    binary_number = [str(number) for number in binary_number]
    return int("".join(binary_number))


stack = Stack()
print(get_binary(stack, 242))
print(type(get_binary(stack, 242)))
