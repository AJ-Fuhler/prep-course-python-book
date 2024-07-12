text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

on line 3, the [start:stop] syntax is being used before the rfind method,
causing the rfind method to iterate over a already sliced string.
This means that the previous index 21 is now index 0. 

On line 4 however, the start and stop arguments from the rfind method 
were used, causing the method to use the indexing of the entire string.


The solution answers the question in a clearer way:

Line 3 first extracts a slice from the text object, ranging from index
21 through index 35. That returns the string 'for the fjords'.
rfind then returns 8, the index of the rightmost instance of an 'f'.

On the other hand, line 4 does a search for the rightmost f between
indexes 21 and 35. Since the f occurs at index 29, that's what 
the method returns.