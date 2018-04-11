import python.datastructures.DS as ds

s1 = ds.Stack()
print(s1.is_empty())
s1.push(4)
s1.push('dog')
print(s1.peek())
print(s1.size())
s1.push(True)
s1.push(8.4)
print(s1.pop())
print(s1.stack)
