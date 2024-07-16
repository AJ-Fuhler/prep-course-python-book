# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# [1, 42, 3]

# Since the dict constructor creates a shallow copy and shallow copies
# only make a duplicate of the outer level, the list assigned to the
# 'a' key in dict2 is a reference to the same exact object in memory
# as the 'a' key in dict1. If you mutate the list by referencing
# either dict1 or dict2, both will reflect that mutation when you print it.