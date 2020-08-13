numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = list(zip(numbers, letters))  #[(1, 'a'), (2, 'b'), (3, 'c')]

zipped2 = zip()
print(list(zipped2)) # []

a = [1, 2, 3]
zipped3 = zip(a)
lst = list(zipped3)  #[(1,), (2,), (3,)]

integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped4 = zip(integers, letters, floats)  # Three input iterables
lst4 = list(zipped4)   #[(1, 'a', 4.0), (2, 'b', 5.0), (3, 'c', 6.0)]

list(zip(range(5), range(100)))  #[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

from itertools import zip_longest
numbers = [1, 2, 3]
alpha = ['a', 'b', 'c']
longest = range(5)
zipped6 = zip_longest(numbers, alpha, longest, fillvalue='?')
list(zipped)     #[(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]


zipped7 = zip(range(3), 'ABCD')
list(zipped)    #[(0, 'A'), (1, 'B'), (2, 'C')]

letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
operators = ['*', '/', '+']
for l, n, o in zip(letters, numbers, operators):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(f'Operator: {o}')

dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)

#unzipping sequence
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(numbers)  #(1, 2, 3, 4)
print(letters)  #('a', 'b', 'c', 'd')

# sorting
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data = sorted(zip(letters, numbers))  # Sort by letters
print(data) # [('a', 4), ('b', 2), ('c', 1), ('d', 3)]

