"""
Like stacks, a queue stores n elements in a single-dimensional structure. The elements are added
and removed in FIFO format. One end of the queue is called the rear and the other is called
the front. When elements are removed from the front, the operation is called dequeue. When
elements are added at the rear, the operation is called enqueue.
"""

class Queue:

    def __init__(self):
        self.items: list = []

    def isEmpty(self) -> bool:
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def representation(self):
        return self.items


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue("Red")
    queue.enqueue('Green')
    queue.enqueue('Blue')
    queue.enqueue('Yellow')
    print(queue.representation())
    print(f"Size of queue is {queue.size()}")
