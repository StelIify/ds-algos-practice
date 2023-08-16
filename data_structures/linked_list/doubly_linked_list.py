class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __repr__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_left(self, node: Node):
        node.next = self.head
        self.head = node

    def insert_right(self, node: Node):
        node.previous = self.tail
        self.tail.next = node
        self.tail = node

    def delete_by_value(self, value):
        if self.head is None:
            return False
        first_el = self.head
        if self.head.data == value:
            self.head = first_el.next
            first_el.next.previous = None
            return True
        while first_el.next:
            next_node = first_el.next
            if next_node.data == value:
                first_el.next = next_node.next
                next_node.next.previous = first_node
                return True
            first_el = first_el.next
        return False

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " <-> ".join(nodes)


d_linked_list = DoublyLinkedList()

first_node = Node("A")
second_node = Node("B")
third_node = Node("C")

first_node.next = second_node
second_node.next = third_node
second_node.previous = first_node
third_node.previous = second_node

d_linked_list.head = first_node
d_linked_list.tail = third_node

d_linked_list.insert_right(Node("D"))
print(d_linked_list)
print(d_linked_list.delete_by_value("C"))
print(d_linked_list)
