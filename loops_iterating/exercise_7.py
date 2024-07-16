my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(sequence):
    my_list = []
    for value in sequence:
        if type(value) is int:
            my_list.append(value)
    return my_list

integers = find_integers(my_tuple)
print(integers)

