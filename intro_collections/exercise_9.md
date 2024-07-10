Question 1: Are the lists assigned to my_list and another_list equal?
Answer: Yes, They are equal because they are both lists with the exact
same elements.

Question 2: Are the lists assigned to my_list and another_list the same object?
Answer: No, the list constructor creates an entirely new object.

Question 3: Are the nested lists at index 3 of my_list and another_list equal?
Answer: Yes, they are equal.

Question 4: Are the nested lists at index 3 of my_list and another_list the 
same object?
Answer: Yes, the list constructor performs a shallow copy, so even though
the list itself is a new object, nested iterables are only references to the
original.
