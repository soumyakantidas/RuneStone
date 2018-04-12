class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return True if self.size() == 0 else False

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def is_not_empty(self):
        return not self.is_empty()


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return True if self.size() == 0 else False

    def is_not_empty(self):
        return not self.is_empty()

    def peek(self):
        return self.queue[-1]

    def clear(self):
        self.queue = []
