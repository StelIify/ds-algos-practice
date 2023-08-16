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

    # one way of implementing that
    # def read(self, index):
    #     if not self.head:
    #         return
    #
    #     current = self.head
    #
    #     for i in range(index):
    #         if not current.next:
    #             return None
    #         current = current.next
    #     return current
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def read(self, index):
        if not self.head:
            return
        for i, node in enumerate(self):
            if i == index:
                return node

    def search(self, value) -> int:
        if self.head is None:
            print("List is empty")
            return -1
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1

    def insert_at_head(self, value: str):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_at_tail(self, value: str):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_at_head(self):
        if self.head is None:
            return
        first_el = self.head
        self.head = first_el.next
        first_el.next = None

    def delete_by_value(self, value):
        if self.head is None:
            return False
        if self.head.data == value:
            self.delete_at_head()
            return True
        current = self.head
        prev = self.head
        while current:
            if current.data == value:
                prev.next = current.next
                current.next = None
                return True
            prev = current
            current = current.next
        return False

    def length(self):
        length = 0
        if not self.head:
            return length
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    # brute force solution
    # def find_mid(self):
    #     length = self.length()
    #     if length % 2 == 0:
    #         mid = length // 2 - 1
    #     else:
    #         mid = length // 2
    #     current = self.head
    #     while mid > 0:
    #         mid -= 1
    #         current = current.next
    #     return current

    # two pointers
    def find_mid(self):
        if not self.head:
            return None
        current = self.head
        if not current.next:
            return current
        # Move mid_node (Slower) one step at a time
        # Move current_node (Faster) two steps at a time
        # When current_node reaches at end, mid_node will be at the middle of List
        mid_node = current
        current = current.next.next
        while current:
            mid_node = mid_node.next
            current = current.next
            if current:
                current = current.next
        if mid_node:
            return mid_node
        return None

    # def remove_duplicates(self):
    #     if not self.head:
    #         return
    #     current = self.head
    #     while current:
    #         inner_node = current
    #         while inner_node:
    #             if inner_node.next:
    #                 if current.data == inner_node.next.data:
    #                     # duplicate found
    #                     inner_node.next = inner_node.next.next
    #                 else:
    #                     inner_node = inner_node.next
    #             else:
    #                 inner_node = inner_node.next
    #         current = current.next

    def remove_duplicates(self):
        if not self.head:
            return None
        current = self.head
        prev = self.head

        visited_nodes = set()
        while current:
            if current.data in visited_nodes:
                prev.next = current.next
                current = current.next
            else:
                visited_nodes.add(current.data)
                prev = current
                current = current.next

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
third_node = Node("B")
forth_node = Node("C")
fifth_node = Node("E")

linked_list.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = forth_node
forth_node.next = fifth_node

print(linked_list)
print(linked_list.insert_at_head("A"))
linked_list.insert_at_tail("E")
print(linked_list)
print(linked_list.delete_by_value("E"))
print(linked_list.delete_by_value("B"))
# linked_list.remove_duplicates()
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
