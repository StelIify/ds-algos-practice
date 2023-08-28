from stack import Stack


def sort_stack(stack):
    sorted_stack = Stack()
    while not stack.is_empty():
        value = stack.pop()
        if sorted_stack.peek() and value >= sorted_stack.peek():
            sorted_stack.push(value)
        else:
            while not sorted_stack.is_empty() and value < sorted_stack.peek():
                stack.push(sorted_stack.pop())
            sorted_stack.push(value)
    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop())
    return stack


stack = Stack()
stack.push(23)
stack.push(60)
stack.push(12)
stack.push(42)
stack.push(4)
stack.push(97)
stack.push(2)
print(sort_stack(stack))
