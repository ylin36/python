# defaultdict is a subclass of dict. it accepts a default_factory as an argument. 
# default_factory can be a primal type or function or lambda

# example with regular dict that maps words who number of occurence in a sentence.
sentence = "she sell sea shells by the sea shore"
words = sentence.split(' ')

dict = {}
for word in words:
    if word in dict:
        dict[word] += 1
    else: # if a key doesn't exist, we need to set it, otherwise the above retrieval and append will cause an error
        dict[word] = 1

print(dict)
# {'she': 1, 'sell': 1, 'sea': 2, 'shells': 1, 'by': 1, 'the': 1, 'shore': 1}

###################
# defaultdict example
###################
from collections import defaultdict

# default dict of type int assigns 0 as value for any key it doesn't have already.
defdict = defaultdict(int)
for word in words:
    defdict[word] += 1

print(defdict)
# defaultdict(<class 'int'>, {'she': 1, 'sell': 1, 'sea': 2, 'shells': 1, 'by': 1, 'the': 1, 'shore': 1})


###################
# defaultdict example with list as type
###################
some_list = [(1, 50, 60), (2, 70, 80), (1, 90, 100), (2, 110, 120), (3, 130, 140)]
defdict2 = defaultdict(list)

for value in some_list:
    for i in range(1, len(value)): # len is O(1) 
        defdict2[value[0]].append(value[i])

print(defdict2)


###################
# defaultdict example with lambda as type
###################

cars = defaultdict(lambda: "rav4")
print(cars["toyota"])
# returns rav4 instead of crashing