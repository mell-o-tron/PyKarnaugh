from karnaugh import simplify


#arity = 3
#expression = lambda a, b, c : not (a or (a and b)) and c

#arity = 2
#expression = lambda a, b : (not a and b) or (not a and b)

#arity = 3
#expression = lambda a, b, c : (not a and b and not c) or (not a and b and c) or (a and not b and not c) or (a and not b and c)


arity = 2
expression = lambda a,b : (a and b)


print(simplify(expression, arity))
