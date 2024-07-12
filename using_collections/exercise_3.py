my_tuple = (1, 2, 3, 4, 5)
reverse_tuple = list(reversed(my_tuple))
reverse_tuple.pop(0)
reverse_tuple.pop()
reverse_tuple = tuple(reverse_tuple)
print(reverse_tuple)

# from solutions, a better solution would be:

my_tuple = (1, 2, 3, 4, 5)
reverse_tuple = list(my_tuple)
reverse_tuple.reverse()
result = tuple(reverse_tuple[1:4])
print(result)

# another solution:

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)

# or:

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:-5:-1]
print(result)