from karnaugh import simplify

print("Half adder:")
arity = 2
out = lambda a, b : 1 if a + b == 1 else 0
remainder = lambda a, b : 1 if a + b == 2 else 0


print("output:")
print(simplify(out, arity))
print("remainder:")
print(simplify(remainder, arity))

print("Full adder:")
arity = 3
out = lambda a, b, c : 1 if (a + b + c == 1) or (a + b + c == 3) else 0
remainder = lambda a, b, c : 1 if a + b + c >= 2 else 0

print("output:")
print(simplify(out, arity))
print("remainder:")
print(simplify(remainder, arity))
