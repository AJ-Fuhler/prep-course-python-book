pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# dict_keys(['Cat', 'Bird', 'Snake'])
# the dict.keys method returns a dictionary view object.
# When you make changes to the dictionary, those changed will be reflected
# right away. So the keys variable was assigned to the .keys method that will
# always return the most current version of the dictionary keys.