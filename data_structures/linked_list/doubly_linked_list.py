class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


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
        print(self.tail)


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