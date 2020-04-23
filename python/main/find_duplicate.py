'''
given string, find duplicates and print index. so for 'a  a b a b c', o/p 'a:[0,1,3], b:[2,4]
'''

def find():

    d = {}
    for i, v in enumerate('a  a b a b c'):
        d_value = []
        if v == ' ':
            continue
        if v in d:
            d_value = d[v]

        d_value.append(i)

        d[v] = d_value
    newDict = {key: value for (key, value) in d.items() if len(value) > 1}
    print('Positions in string: {}'.format(newDict))

def find02():
    ar = 'a  a b a b c'.split()

    d = {}
    for i, v in enumerate(ar):
        d_value = []
        if v in d:
            d_value = d[v]
        d_value.append(i)

        d[v] = d_value
    newDict = {key: value for (key, value) in d.items() if len(value) > 1}
    print('Positions in array: {}'.format(newDict))

def find03(str):
    lst = list(str)
    s = set(lst)
    d = {}
    for e in s:
        if ' ' not in e and lst.count(e) > 1:
            pos = [ i for i,v in enumerate(lst) if e in v]
            d[e] = pos
    return d

#newDict = filterTheDict(dictOfNames, lambda elem : elem[0] % 2 == 0)
# newDict = filterTheDict(dictOfNames, lambda elem: elem[1]>1) requires extra method


find()

find02()
print(find03('a  a b a b c'))