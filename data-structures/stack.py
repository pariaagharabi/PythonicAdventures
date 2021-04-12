class Stack:
    def __init__(self):
        self.stack = []

    def print(self):
        print(self.stack)

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def reverse(self):
        items = []

        while not self.is_empty():
            items.append(self.pop())
        for item in items:
            self.push(item)
