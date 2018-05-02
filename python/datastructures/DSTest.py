from python.datastructures.DS import BinaryTree, MinHeap, MaxHeap, BinarySearchTree
from random import randint, seed

seed(1)

# s1 = ds.Stack()
# print(s1.is_empty())
# s1.push(4)
# s1.push('dog')
# print(s1.peek())
# print(s1.size())
# s1.push(True)
# s1.push(8.4)
# print(s1.pop())
# print(s1.stack)

# l1 = ds.LinkedList()
# l1.add(31)
# l1.add(77)
# l1.add(17)
# l1.add(93)
# l1.add(26)
# l1.add(54)
#
# print(l1)
# print(l1.size())
# print(l1.search(76))
# # l1.remove(93)
# l1.reverse()
# print("reversed:", l1)

# bt = BinaryTree(50)
# seed(1)
#
# for _ in range(50):
#     value = randint(0, 100)
#     # print(value)
#     bt.add(value)
#
# print(bt)
#
# bt.preorder()

# mh = MinHeap()
# mh.heapify([randint(0, 100) for _ in range(100)])
# # mh.insert()
# # mh.remove()
# print(mh)
# print([mh.remove() for _ in range(101)])

# mh = MaxHeap()
# mh.heapify([randint(0, 100) for _ in range(100)])
# # mh.remove()
# # mh.heapify([1, 4, 3, 5, 2, 4])
# print(mh)
# print([mh.remove() for _ in range(100)])
# # print(mh)

bst = BinarySearchTree()
# for i in range(10):
#     num = randint(1, 10)
#     print(num)
#     bst[num] = num
#
# print("pre-order:", bst.preorder())
# print("in-order:", bst.inorder())
# print("post-order:", bst.postorder())
#
# print(bst[20])
# print(20 in bst)
# bst[2] = 4
# bst[3] = 9
# bst[1] = 1
# # bst[3] = 9
# del bst[2]
# print(bst[2])
# print(bst[3])
for i in [17, 5, 35, 2, 11, 29, 38, 9, 16, 7, 8]:
    bst[i] = i

print("pre-order:", bst.preorder())
print("in-order:", bst.inorder())
print("post-order:", bst.postorder())
print(bst.height())
# del bst[35]
# print("pre-order:", bst.preorder())
