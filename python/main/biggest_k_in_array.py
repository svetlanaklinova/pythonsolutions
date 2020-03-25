




def find(ar, k):
    if not ar or k == 0:
        return None
    s = set(ar)
    if k >= len(s):
        return None
    while k != 0:
        s.remove(max(s))
        k -= k
    return max(s)

assert  find([5,5,-1,1,0,0], 2) ==  1
assert  find([5,-1,1,1,0], 4) ==  None
assert  find([5,-1,1,0], 4) ==  None
assert  find([5,-1,1,0], 0) == None
assert  find([5,-1], 2) == None
assert  find([5], 2) == None
assert  find([], 2) == None
assert  find([-3,-1,-8,0], 2) ==  -1