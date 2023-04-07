# Although, we can use a list in python for a stack it is more efficient on memory management to use a doubly linked list/ deque from python

from collections import deque

stack = deque()

stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('https://www.cnn.com/china')

print(stack)
print(stack.pop())
