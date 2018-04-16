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


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return True if self.head is None else False

    def is_not_empty(self):
        return not self.is_empty()

    def add(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def search(self, key):
        current = self.head
        found = False
        while not found and current is not None:
            if current.value == key:
                found = True
                break
            else:
                current = current.next

        return found

    def remove(self, key):
        previous = None
        current = self.head
        found = False
        while not found and current is not None:
            if current.value == key:
                found = True
                break
            else:
                previous = current
                current = current.next

        if found:
            previous.next = current.next



    def __str__(self):
        li = []
        current = self.head
        while current is not None:
            li.append(current.value)
            current = current.next

        return " -> ".join(map(str, li))
