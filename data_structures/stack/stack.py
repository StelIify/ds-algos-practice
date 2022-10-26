class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        """Inserts an item on top of the stack"""
        self._items.append(item)

    def pop(self):
        """Removes and returns an item from top of the stack"""
        return self._items.pop()

    def peek(self):
        """ Returns top item of the stack"""
        if not self.is_empty():
            return self._items[-1]

    def get_stack(self):
        return self._items

    def is_empty(self):
        return self._items == []


# new_stack = stack()
# new_stack.push(44)
# new_stack.push(23)
# print(new_stack.peek())
# new_stack.pop()
# print(new_stack.peek())