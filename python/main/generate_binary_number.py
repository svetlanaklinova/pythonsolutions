
from itertools import product
from functools import reduce

def generate_binary(length):
    lst = list(product([0,1], repeat=length))
    result = []
    for l in lst:
        result.append(reduce(lambda x,y: str(x) + str(y), l, ''))
    return result

def check_is_repeatable(str):
    s = list(str)
    l = len(str)
    for i in range(l):
        if l-1 > i and s[i] == s[i+1] and s[i] == '0':
            return True
    return False

def exclude_zero_start_and_contin(num):
    lst = generate_binary(num)
    result = []
    for l in lst:
        if  l.startswith('0') or check_is_repeatable(l):
            continue
        result.append(l)
    return result

print(exclude_zero_start_and_contin(4))