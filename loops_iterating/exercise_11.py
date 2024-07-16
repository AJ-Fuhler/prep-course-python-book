my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

even_numbers = []
index = 0
while index < len(my_list):
    nested_index = 0
    while nested_index < len(my_list[index]):
        if my_list[index][nested_index] % 2 == 0:
            even_numbers.append(my_list[index][nested_index])
        nested_index += 1
    index += 1

print(even_numbers)