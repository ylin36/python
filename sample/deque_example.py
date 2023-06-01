# "Decks" generalization of stack and queue. it replaces list, support memory efficient push and pop to both ends.

from collections import deque
import string

d = deque("abc")
for letter in d:
    print(letter)

# a
# b
# c

print(d)
# deque(['a', 'b', 'c'])

d.append("hello world")
print(d)
# deque(['a', 'b', 'c', 'hello world'])


e = deque(['ab','cd'])
print(e)
# deque(['ab', 'cd'])

e.appendleft('ef')
print(e)
# deque(['ef', 'ab', 'cd'])



with open('print.py') as f:
    deq = deque(f, 2)

print(deq)
# deque(['print("hello", end=" ")\n', 'print("world")'], maxlen=2)

print(deq.popleft())
# print("hello", end=" ")
