obj = 'ABcd' = reassignment
obj.upper() = nothing, simply returns a copy with all uppercase
obj = obj.lower() = reassignment
print(len(obj)) = nothing, simply returns length of object (4)
obj = list(obj) = reassignment, strings are immutable
obj.pop() = mutation
obj[2] = 'X' = mutation
obj.sort() = mutation
set(obj) = nothing, simply returns a copy of obj as a set
obj = tuple(obj) = reassignment