''' Print all subsets of array'''


def sub_sets(sset):
    return subsetsRecur([], sorted(sset))


def subsetsRecur(current, sset):
    if sset:
        return subsetsRecur(current, sset[1:]) + subsetsRecur(current + [sset[0]], sset[1:])
    return [current]

# print(sub_sets([1,2,3]))
assert sub_sets([1,2,3]) == [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

