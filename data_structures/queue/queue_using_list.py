class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def read(self):
        if self._items:
            return self._items[0]


class PrintManager:
    def __init__(self):
        self.queue = Queue()

    def queue_print_job(self, document):
        self.queue.enqueue(document)

    def run(self):
        while self.queue.read():
            print(self.queue.dequeue())


print_manager = PrintManager()
print_manager.queue_print_job("First Document")
print_manager.queue_print_job("Second Document")
print_manager.queue_print_job("Third Document")
print_manager.run()