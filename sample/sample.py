import os
from functools import reduce

print('current directory')
print(os.getcwd())

some_list = [1, 2, 3, 4]
sum = reduce(lambda n1, n2: n1 + n2, some_list)
print(sum) # 10