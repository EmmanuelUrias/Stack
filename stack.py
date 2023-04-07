# In python you can use a list as a stack. I will store a users url history
stack = []

stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('https://www.cnn.com/china')

print(stack)
print(stack[-1])

stack.pop()

print(stack)

stack.pop()

print(stack)
