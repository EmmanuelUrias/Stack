from collections import deque

string = 'We will conquere COVID-19'


def reverse_string(string):
    stack = deque()

    for char in string:
        stack.append(char)

    reversed_str = ''
    while len(stack) != 0:
        reversed_str += stack.pop()

    return reversed_str


print(reverse_string(string))
