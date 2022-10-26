class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head

        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist.")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def count_nodes(self):
        if self.head is None:
            return
        node_count = 0
        current = self.head
        while current is not None:
            current = current.next
            node_count += 1
        return node_count


linked_list = LinkedList()

linked_list.append("B")
linked_list.append("D")
linked_list.append("E")
linked_list.prepend("A")

linked_list.insert_after_node(linked_list.head.next, "C")

linked_list.print_list()
print(linked_list.count_nodes())
