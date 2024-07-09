def even_or_odd(number):
    if (number % 2 == 0):
        print('even')
    else:
        print('odd')

even_or_odd(4)
even_or_odd(5)
even_or_odd(22)
even_or_odd(37)
print()

def even_or_odd_match(number):
    match (number % 2 == 0):
        case True:
            print('even')
        case _: print('odd')

even_or_odd_match(4)
even_or_odd_match(5)  
even_or_odd_match(22)          
even_or_odd_match(37)  
print()

def even_or_odd_ternary(number):
    print('even' if number % 2 == 0 else 'odd')

even_or_odd_ternary(4)
even_or_odd_ternary(5)
even_or_odd_ternary(22)
even_or_odd_ternary(37)