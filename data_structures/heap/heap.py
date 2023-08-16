class Heap:
    def __init__(self):
        self.data = []

    def last_node(self):
        return len(self.data) - 1

    @staticmethod
    def left_child(index):
        return 2 * index + 1

    @staticmethod
    def right_child(index):
        return 2 * index + 2

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    def insert(self, value):
        ...

    def delete(self):
        ...


class MaxHeap(Heap):
    def __init__(self):
        super().__init__()
        self.data = [100, 80, 70, 60]

    def insert(self, value):
        self.data.append(value)

        new_value_index = self.last_node()
        parent_index = self.parent(new_value_index)
        while new_value_index > 0 and self.data[new_value_index] > self.data[parent_index]:
            self.data[new_value_index], self.data[parent_index] = self.data[parent_index], self.data[new_value_index]

            new_value_index = parent_index
            parent_index = self.parent(new_value_index)

    def heapify_up(self, index):
        if index == 0:
            return

        parent_index = self.parent(index)
        parent_value = self.data[parent_index]

        new_value = self.data[index]

        if new_value > parent_value:
            self.data[index] = parent_value
            self.data[parent_index] = new_value
            self.heapify_up(parent_index)

    def insert_recursive(self, value):
        self.data.append(value)
        self.heapify_up(self.last_node())

    def pop(self):
        deleted_value = self.data[0]
        self.data[0] = self.data.pop(self.last_node())

        heapify_idx = 0
        left_child = self.left_child(heapify_idx)
        right_child = self.right_child(heapify_idx)

        while heapify_idx < len(self.data) - 1 and self.data[left_child] > self.data[right_child]:
            self.data[heapify_idx], self.data[left_child] = self.data[left_child], self.data[heapify_idx]
            heapify_idx = left_child
            left_child = self.left_child(heapify_idx)
            right_child = self.right_child(heapify_idx)

        while heapify_idx < len(self.data) - 1 and left_child <= self.last_node():

            if right_child <= self.last_node() and self.data[left_child] < self.data[right_child]:
                larger_child = right_child
            else:
                larger_child = left_child

            if self.data[larger_child] > self.data[heapify_idx]:
                self.data[heapify_idx], self.data[larger_child] = self.data[larger_child], self.data[heapify_idx]
                heapify_idx = larger_child
                left_child = self.left_child(heapify_idx)
                right_child = self.right_child(heapify_idx)
            else:
                break

        return deleted_value


max_heap = MaxHeap()
max_heap.insert(110)
print(max_heap.data)
max_heap.insert(90)
print(max_heap.data)
print(max_heap.pop())
print(max_heap.data)


