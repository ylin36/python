# code example using named tuple to convert a dict into object

from collections import namedtuple

Parts = {'id_num':'1', 'desc':'Gas Engine',
     'cost':2000.00, 'amount':1}
parts = namedtuple('Parts', Parts.keys())(**Parts)
print(type(parts)) # <class '__main__.Parts'>
print(type(Parts)) # <class 'dict'>
print(parts)
