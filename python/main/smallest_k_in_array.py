

def find(arr, num):
    k = num
    while k > 1:
        arr.remove(min(arr))
        k -= 1

    return min(arr) if arr and num else None


assert (find([2,4,9,0,3,1],0)== None) ## None
assert (find([],0)== None) ## None
assert (find([2,4,9,0,3,1],2)==1) ## 1