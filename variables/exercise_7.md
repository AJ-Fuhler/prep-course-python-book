It will print out Good Morning, Afternoon and Evening, Victor first.
Then it will print out Good Morning, Afternoon and Evening, Nina.
Despite it looking like the intention was for NAME to be a constant,
Python does not natively have constants, so you'd have to make sure
you don't reassign a constant yourself.
If this identifier needs to be changed, use a regular variable (e.g. name)