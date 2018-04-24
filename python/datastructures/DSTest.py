import python.datastructures.DS as ds

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

l1 = ds.LinkedList()
l1.add(31)
l1.add(77)
l1.add(17)
l1.add(93)
l1.add(26)
l1.add(54)

print(l1)
print(l1.size())
print(l1.search(76))
# l1.remove(93)
l1.reverse()
print("reversed:", l1)

