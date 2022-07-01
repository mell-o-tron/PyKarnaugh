import math
import itertools

#==================================#
# Generates Gray codes. Not currently used
def gray (n):
    if n == 1:
        return [[0], [1]]
    else:
        res = []
        L1 = gray(n-1)
        L2 = L1.copy()
        L2.reverse()
        for l in L1:
            res.append([0] + l)
        for l in L2:
            res.append([1] + l)
        return res


#==================================#
# Generates the good ole 000 001 010 011 ...
# Not optimal because I have to transpose the resulting table
def generate_table(arity):
    A = []
    for i in range(-arity, 0):
        i = -i
        B = []

        for j in range(2 ** arity):
            if j % 2**i < 2 ** (i-1):
                B.append(0)
            else:
                B.append(1)
        A.append(B)
    return A

#==================================#
# Generates the truth table of an expression.
def truth_table(exp, arity):
    A = generate_table(arity)
    res = []
    for i in range(2 ** arity):
        arg = []
        for j in range(arity):
            arg.append(A[j][i])
        res.append(1 if expression(*arg) else 0)

    return res

#==================================#
# Generates an empty n-dimensional list
def empty_n_list(n):
    if n == 1:
        return [0, 0]

    res = []
    for i in range(n):
        A = empty_n_list(n-1)
        res += [A.copy()]
    return res


#==================================#
# Sets an element of an n-dimensional list
def set_elem_n_list(A, b, value):
    if len(b) == 1:
        A[b[0]] = value
        return
    else:
        set_elem_n_list(A[b[0]], b[1:], value)


#==================================#
# Generates the karnaugh map of an expression.
# For n > 2, it does not really look like a k-map one might draw on paper

def k_map (exp, arity):
    M = empty_n_list(arity)
    A = generate_table(arity)
    for i in range(2 ** arity):
        arg = []
        for j in range(arity):
            arg.append(A[j][i])
        set_elem_n_list(M, arg, 1 if exp(*arg) else 0)
    return M

#==================================#
# Checks if the element at position b (vector) is 1
def k_map_is_elem_1(A, b):
    if len(b) == 1:
        return A[b[0]] == 1
    else:
        return k_map_is_elem_1(A[b[0]], b[1:])


#==================================#
# Finds the largest sphere(s) of ones in a k-map
def find_largest_sphere(A, b):

    if len(b) == 0:
        for i in range(len(A)):
            b.append(2)     # 2 = not fixed
    len_b = len(b)

    nn2 = 0
    for i in range(len_b):
        if b[i] != 2:
            nn2 += 1

    if nn2 == len_b and k_map_is_elem_1(A, b):
        return [b]
    elif nn2 == len_b:
        return []
    #else:
        #print(f"b is: {b}")
    #print()

    l = len(b) - nn2
    new_T = generate_table(l)
    for i in range(len_b):
        if b[i] != 2:
            newColumn = []
            for j in range(len(new_T[0])):
                newColumn.append(b[i])
            new_T.insert(i, newColumn)

    #print(f"the new T is: {new_T}")

    all_ones = True
    #print("args:")
    for i in range(2 ** l):
        arg = []
        for j in range(len_b):
            arg.append(new_T[j][i])
        #print(arg)
        all_ones = all_ones and k_map_is_elem_1(A, arg)

    if all_ones:
        #print("all ones!")
        return [b]

    if not all_ones:
        #print("not all ones...\n")

        elem_list = []
        list_2s = []
        for i in range(len_b):
            if b[i] != 2:
                continue
            new_b_0 = b.copy()
            new_b_1 = b.copy()

            new_b_0[i] = 0
            new_b_1[i] = 1

            elem_list += find_largest_sphere(A, new_b_0)
            elem_list += find_largest_sphere(A, new_b_1)

        # sort and remove duplicates...
        elem_list.sort()
        elem_list = list(elem_list for elem_list,_ in itertools.groupby(elem_list))

        max2 = 0
        maxi = 0
        for i in range(0, len(elem_list)):
            num2 = 0
            for j in elem_list[i]:
                if j == 2:
                    num2 += 1
            list_2s.append(num2)
            if num2 > max2:
                max2 = num2
                maxi = i

        final_spheres = []
        for i in range(len(elem_list)):
            #print(f"{elem_list[i]} \t {list_2s[i]}")
            if list_2s[i] == max2:
                final_spheres.append(elem_list[i])

        #print()

        return final_spheres

#==================================#
# "Simplifies" an expression.

def simplify(exp, arity):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
    if arity > 8:
        print("Too many variables, I'm too lazy")
        return ""
    M = k_map(exp, arity)
    S = find_largest_sphere(M, [])

    S.sort()
    result = ""

    for i in range(len(S)):
        if i > 0:
            result += " + "
        for j in range(len(S[i])):
            if S[i][j] == 1:
                result += alphabet[j]
            elif S[i][j] == 0:
                result += (f"(~{alphabet[j]})")
    return result


