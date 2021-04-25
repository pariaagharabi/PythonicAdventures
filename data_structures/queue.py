class Queue:
    def __init__(self):
        self.queue = []

    def print(self):
        print(self.queue)

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def reverse(self):
        items = []

        while not self.is_empty():
            items.insert(0, self.dequeue())
        for item in items:
            self.enqueue(item)

    # Reversing the first K elements of a Queue
    def reverse_first_k_elements(self, k):
        if (self.is_empty() == True or k > self.size()):
            return
        if (k <= 0):
            return self.is_empty
