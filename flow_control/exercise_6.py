def str_upper(string):
    if len(string) > 10:
        new_string = string
        return new_string.upper()
    else:
        return string
    

print(str_upper('abcdefghij'))
print(str_upper('abcdefghijk'))

# I chose to assign a new variable new_string in order to prevent
# mutating the argument with the upper method.