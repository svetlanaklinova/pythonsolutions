# lists
l1 = [1,2,3]
l2 = [4,5,6]

ls = l1 + l2
print(ls) # [1, 2, 3, 4, 5, 6]

#tuples
t1 = (1,2,3,4)
t2 = (4,5,6,7)
t_ls = t1 + t2
print(t_ls) # (1, 2, 3, 4, 4, 5, 6, 7)

t_unique_ls = set(t_ls)
print(t_unique_ls) # {1, 2, 3, 4, 5, 6, 7}

#dict
d2 = {'d':4, 'e':5, 'o':1}
d3 = {'k':24, 'm':26, 'o':4}
d_join = {**d2, **d3}
print(d_join) # {'d': 4, 'e': 5, 'o': 4, 'k': 24, 'm': 26}





