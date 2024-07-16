 # What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict)) 

# CHRIS

# 1. We call dictionary.keys ti see all the keys of the dictionary object.
# 2. we use composition to call sorted on the dictionary view to get a
#    sorted list of the keys in the dictionary object.
# 3. We use chaining to get the dict key at index position 1 and call
#    the upper method on that key.