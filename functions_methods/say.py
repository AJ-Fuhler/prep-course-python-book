def say():
    """
    The say function prints "Hi!"
    """
    print('Output from say')

print('First')
say()
print('Last')
print(say.__doc__)
print('-' * 60)
help(say)