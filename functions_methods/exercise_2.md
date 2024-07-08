This program will print 'bar'. Inside the function a new variable 'foo'
is assigned to the value 'qux'. It does not affect the foo variable
in the lexical scope. This is called variable shadowing. The foo variable on
line 4 shadows the foo variable on line 1 and therefor does not change the value
of foo from line 1.
