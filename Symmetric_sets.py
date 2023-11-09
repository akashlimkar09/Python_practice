#type 1
def sym(set1, set2):
    return set(set1) - set(set2) | set(set2) - set(set1)

A = {1, 2, 3}
B = {5, 2, 1, 4}
output = sym(A, B)
print(output)

C={2,2,3,4,5}
D={2,8,5,6}
output = sym(D, C)
print(output)

#type 2
def symmetric_difference_sets(*sets):
    result = set()

    # Combine all elements from input sets into the result set
    for s in sets:
        for element in s:
            if element not in result:
                result.add(element)
            else:
                result.remove(element)

    return result

set_A = {1, 2, 3}
set_B = {5, 2, 1, 4}
set_C = {3, 4, 6}
set_D = {7, 8, 9}

output = symmetric_difference_sets(set_A, set_B, set_C, set_D)
print(output)
