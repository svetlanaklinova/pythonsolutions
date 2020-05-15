''' Generate and print all subsets of array
input:
[1,2,3]
output:
[[], [2], [3], [1], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

'''

from itertools import chain, combinations

def subset(iterable):
    lstTuples = \
        list(
            chain.from_iterable(
                set(combinations(iterable, r)) for r in range(len(iterable) + 1)
            )
        )
    s = [ list(aTuple) for aTuple in lstTuples]

    print(s)
    return s


assert subset([1,2,3]) == [[], [2], [3], [1], [1, 2], [1, 3], [2, 3], [1, 2, 3]]


