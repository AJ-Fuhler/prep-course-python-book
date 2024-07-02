It would get an error:
(ValueError: invalid literal for int() with base 10: '3.1415')
This is because the int function is expecting a string with an integer,
instead it is finding a floating point number.