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


class TreeNode:
    """
    TreeNode is a Binary Node class with key, value, left, right and parent parameters
    """
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def has_left(self):
        return self.left

    def has_right(self):
        return self.right

    def is_left(self):
        return self.parent and self.parent.has_left() == self

    def is_right(self):
        return self.parent and self.parent.has_right() == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.has_left() or self.has_right())

    def has_any_children(self):
        return not self.is_leaf()

    def has_both_children(self):
        return self.has_left() and self.has_right()

    def set_node(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        if self.has_left():
            self.left.parent = self
        if self.has_right():
            self.right.parent = self

    def preorder(self, node, li):
        if node:
            li.append(node.value)
            self.preorder(node.left, li)
            self.preorder(node.right, li)

    def inorder(self, node, li):
        if node:
            self.inorder(node.left, li)
            li.append(node.value)
            self.inorder(node.right, li)

    def postorder(self, node, li):
        if node:
            self.postorder(node.left, li)
            self.postorder(node.right, li)
            li.append(node.value)

    def find_min(self):
        current = self
        while current.has_left():
            current = current.left
        return current

    def find_successor(self):
        successor = None
        if self.has_right():
            successor = self.right.find_min()
        else:
            if self.parent:
                if self.is_left():
                    successor = self.parent
                else:
                    self.parent.right = None
                    successor = self.parent.find_successor()
                    self.parent.right = self
        return successor

    def splice_out(self):
        if self.is_leaf():
            if self.is_left():
                self.parent.left = None
            else:
                self.parent.right = None
        else:
            if self.has_left():
                if self.is_left():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.is_left():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def height(self, node):
        if node:
            h_left = self.height(node.left)
            h_right = self.height(node.right)
            return max(h_left, h_right) + 1
        else:
            return -1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return True if self.get(key) else None

    def __delitem__(self, key):
            self.delete(key)

    def put(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
            self.size += 1
        else:
            self._put(key, value, self.root)

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left():
                self._put(key, value, current_node.has_left())
            else:
                current_node.left = TreeNode(key, value, parent=current_node)
                self.size += 1
        elif key == current_node.key:
            current_node.value = value
        else:
            if current_node.has_right():
                self._put(key, value, current_node.has_right())
            else:
                current_node.right = TreeNode(key, value, parent=current_node)
                self.size += 1

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            return result.value if result else None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self._remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("key not present")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("key not present")

    @staticmethod
    def _remove(node):
        if node.is_leaf():
            if node.is_left():
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.has_both_children():
            successor = node.find_successor()
            successor.splice_out()
            node.key = successor.key
            node.value = successor.value
        else:
            if node.has_left():
                if node.is_left():
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.is_right():
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:
                    node.set_node(node.left.key, node.left.value, node.left.left, node.left.right)
            else:
                if node.is_left():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.is_right():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.set_node(node.right.key, node.right.value, node.right.left, node.right.right)

    def preorder(self):
        li = []
        if self.root:
            self.root.preorder(self.root, li)
            return li
        else:
            raise KeyError("Tree is empty")

    def inorder(self):
        li = []
        if self.root:
            self.root.inorder(self.root, li)
            return li
        else:
            raise KeyError("Tree is empty")

    def postorder(self):
        li = []
        if self.root:
            self.root.postorder(self.root, li)
            return li
        else:
            raise KeyError("Tree is empty")

    def height(self):
        if self.size > 0:
            return self.root.height(self.root)
        else:
            raise RuntimeError("Empty Tree")


class Vertex:
    def __init__(self, key):
        self.key = key
        self.connections = {}

    def __str__(self):
        return "{} connected to {}".format(self.key, list(self.connections.items()))

    def add_neighbour(self, neighbour, weight=0):
        self.connections[neighbour] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_weight(self, neighbour):
        return self.connections[neighbour]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.size = 0

    def __contains__(self, key):
        return key in self.vertices

    def __str__(self):
        result = []
        for key in self.vertices.keys():
            result.append(self.vertices[key].__str__())
        return "\n".join(result)

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vertices.get(key, None)

    def add_edge(self, from_, to, weight=0):
        if from_ not in self.vertices:
            self.add_vertex(from_)
        if to not in self.vertices:
            self.add_vertex(to)
        self.vertices[from_].add_neighbour(to, weight)

    def get_vertices(self):
        return self.vertices.keys()
