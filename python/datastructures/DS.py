from random import randint


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

    def __str__(self):
        if self.next is None:
            return "{}  ----->  {}".format(self.value, self.next)
        else:
            return "{}  ----->  {}".format(self.value, self.next.value)


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

    def reverse(self):
        if self.head is None or self.head.next is None:
            pass
        else:
            prev = None
            curr = self.head
            while curr is not None:
                # print("prev:", prev, "curr:", curr)
                rem = curr.next
                curr.next = prev
                prev = curr
                curr = rem
                # print("prev:", prev, "curr:", curr)

            self.head = prev

    def __str__(self):
        li = []
        current = self.head
        while current is not None:
            li.append(current.value)
            current = current.next

        return " -> ".join(map(str, li))


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        if self.left is None and self.right is not None:
            return "{} --> {}".format(self.value, self.right.value)
        if self.left is not None and self.right is None:
            return "{} <-- {}".format(self.left.value, self.value)
        if self.left is not None and self.right is not None:
            return "{} <-- {} --> {}".format(self.left.value, self.value, self.right.value)


class BinaryTree:
    def __init__(self, value):
        self.root = BinaryNode(value)

    def insert_left(self, value):
        if self.root.left is None:
            self.root.left = BinaryNode(value)
        else:
            temp_node = BinaryNode(value)
            temp_node.left = self.root.left
            self.root.left = temp_node

    def insert_right(self, value):
        if self.root.right is None:
            self.root.right = BinaryNode(value)
        else:
            temp_node = BinaryNode(value)
            temp_node.right = self.root.right
            self.root.right = temp_node

    def _add(self, value):
        current = self.root
        while current is not None:
            if value < current.value:
                if current.left is None:
                    current.left = BinaryNode(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = BinaryNode(value)
                    break
                else:
                    current = current.right

    def add(self, value):
        current = self.root

        while current is not None:
            if current.left is None and current.right is None:
                choice = randint(0, 1)
                if choice == 0:
                    current.left = BinaryNode(value)
                    break
                else:
                    current.right = BinaryNode(value)
                    break
            elif current.left is None:
                current.left = BinaryNode(value)
                break
            elif current.right is None:
                current.right = BinaryNode(value)
                break
            else:
                choice = randint(0, 1)
                if choice == 0:
                    current = current.left
                else:
                    current = current.right

    def preorder(self):
        print(self.root.value)
        if self.root.left:
            self.root.left.preorder()
        if self.root.right:
            self.root.right.preorder()

    def __str__(self):
        result = []
        current = self.root
        result.append(current.__str__())
        while current.left is not None:
            current = current.left
            result.append(current.__str__())
        current = self.root
        while current.right is not None:
            current = current.right
            result.append(current.__str__())
        return "\n".join(result)


class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def _percolate_up(self):
        i = self.size
        while i // 2 > 0:
            if self.heap[i//2] > self.heap[i]:
                self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i //= 2

    def _percolate_down(self, i):
        while 2*i <= self.size:
            mc = self._min_child(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def _min_child(self, i):
        if 2*i+1 > self.size:
            return 2*i
        else:
            if self.heap[2*i] < self.heap[2*i+1]:
                return 2*i
            else:
                return 2*i+1

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self._percolate_up()

    def peek(self):
        if self.size >= 1:
            return self.heap[1]

    def remove(self):
        if self.size >= 1:
            result = self.heap[1]
            self.heap[1] = self.heap[-1]
            self.size -= 1
            self.heap.pop()
            self._percolate_down(1)
            return result

    def heapify(self, array):
        i = len(array) // 2
        self.heap = [0] + array[:]
        self.size = len(array)
        while i > 0:
            self._percolate_down(i)
            i -= 1

    def __str__(self):
        return " ".join(map(str, self.heap[1:]))


class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def _percolate_up(self):
        i = self.size
        while i//2 > 0:
            if self.heap[i] > self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i //= 2

    def _percolate_down(self, i):
        while 2*i <= self.size:
            mc = self._max_child(i)
            if self.heap[i] < self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def _max_child(self, i):
        if 2*i+1 > self.size:
            return 2*i
        else:
            if self.heap[2*i] > self.heap[2*i+1]:
                return 2*i
            else:
                return 2*i+1

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self._percolate_up()

    def remove(self):
        if self.size >= 1:
            result = self.heap[1]
            self.heap[1] = self.heap[-1]
            self.heap.pop()
            self.size -= 1
            self._percolate_down(1)
            return result

    def peek(self):
        if self.size >= 1:
            return self.heap[1]

    def heapify(self, array):
        i = len(array) // 2
        self.heap = [0] + array[:]
        self.size = len(array)
        while i > 0:
            self._percolate_down(i)
            i -= 1

    def __str__(self):
        return " ".join(map(str, self.heap[1:]))
