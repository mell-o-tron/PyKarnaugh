# PyKarnaugh
Boolean algebra simplifier based on n-dimensional k-maps

## Usage

Define a boolean function in python, e.g. `lambda a, b, c : not (a or (a and b)) and c`, and pass it, along with its *arity* (that is, the number of its parameters) to the `simplify` function, which will return a string containing the result of the simplification, in disjunctive normal form.
