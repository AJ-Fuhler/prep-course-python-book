# Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

# The life of brian

# the dict constructor creates a shallow copy, so it creates a duplicate
# of the outer layer in dict1. Since they are separate objects, if you
# assign a different value to the 'Monthy Python' key in dict2, dict1
# will not be affected.