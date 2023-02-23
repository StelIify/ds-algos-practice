from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


linked_list = LinkedList()

first_node = Node("A")
second_node = Node("B")
third_node = Node("C")
forth_node = Node("D")
fifth_node = Node("E")

linked_list.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = forth_node
forth_node.next = fifth_node

print(linked_list)


def reverse_list(head: Optional[Node]) -> Optional[Node]:
    current = head
    previous = None

    while current:
        next_node = current.next

        current.next = previous

        previous = current

        current = next_node

    return previous


reverse_list(linked_list.head)
print(linked_list)





