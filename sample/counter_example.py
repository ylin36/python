from collections import Counter

print(Counter("hello world"))
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

counter = Counter("hello world")
print(counter["e"])
# 1

print(counter.elements())
# <itertools.chain object at 0x000001DC75E01EE0>

print(list(counter.elements()))
# ['h', 'e', 'l', 'l', 'l', 'o', 'o', ' ', 'w', 'r', 'd']

top_n_occuring = 2
print(counter.most_common(top_n_occuring))
# [('l', 3), ('o', 2)]

counter_two = Counter("world")
counter.subtract(counter_two) # this method mutate the subtractor
print(counter) # notice the number have decreased
# Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1, ' ': 1, 'w': 0, 'r': 0, 'd': 0})