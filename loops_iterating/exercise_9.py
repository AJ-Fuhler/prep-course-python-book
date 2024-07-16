def factorial(number):
    my_list = list(range(2, number + 1))
    index = 0
    result = 1
    while index < len(my_list):
        result *= my_list[index]
        index += 1
    return result

print(factorial(4))
print(factorial(5))

# Now the more readable function with a for loop:

def fortorial(number):
    result = 1
    for num in range(2, number + 1):
        result *= num
    return result

print(fortorial(4))
print(fortorial(5))


# Now the provided solution, but with one less iteration:

def factor(n):
    result = 1
    for number in range(n, 1, -1):
        result *= number
    
    return result

print(factor(4))
print(factor(5))

