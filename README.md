# PyKarnaugh
Boolean algebra simplifier based on n-dimensional k-maps

## Usage

Define a boolean function in python, e.g. `lambda a, b, c : not (a or (a and b)) and c`, and pass it, along with its *arity* (that is, the number of its parameters) to the `simplify` function, which will return a string containing the result of the simplification, in disjunctive normal form.

## Examples
`k_user.py` contains two examples: the half and full adder. As a simple usage example, here is the full adder (`c` is the input remainder):

```python
arity = 3
out = lambda a, b, c : 1 if (a + b + c == 1) or (a + b + c == 3) else 0
remainder = lambda a, b, c : 1 if a + b + c >= 2 else 0

print("output:")
print(simplify(out, arity))
print("remainder:")
print(simplify(remainder, arity))
```

The output will be:

```Full adder:
output:
(~A)(~B)C + (~A)B(~C) + A(~B)(~C) + ABC
remainder:
AB + AC + BC
```
