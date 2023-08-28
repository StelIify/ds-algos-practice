from queue_using_deque import Queue


def reverse_first_k_elements(queue, k):
    reversed_el = []
    for _ in range(k):
        reversed_el.append(queue.dequeue())
    while len(reversed_el) > 0:
        queue.enqueue(reversed_el.pop())
    for _ in range(k):
        queue.enqueue(queue.dequeue())
    return queue


queue = Queue()
for i in range(1, 11):
    queue.enqueue(i)
print(reverse_first_k_elements(queue, 5))
