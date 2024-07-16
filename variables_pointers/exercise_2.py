# Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# {42, 'Monthy Python', ('a', 'b', 'c'), range(5,10)}
# This is because when you assign a variable with another variable, 
# they reference the same object in memory. They reference the same set.