

l_tup_int = (1,2,3,4)
l_tup_str = ('1','2','3')




f = list(map(lambda x: x*x,l_tup_int))
f1 = list(map(lambda x: '1' not in x,l_tup_str))

print(f)
print('f1 {}'.format(f1))
# lists
## strings
l_string = ['1','2','3','4']

f_str = list(map(lambda x: int(x)*int(x), l_string))

## int
print('Integers')
l_int = [1,2,3,4]
str_int = list(map(lambda x : len(str(x)), l_int))
print(str_int)
f_int = list(map(lambda x: int(x)*int(x), l_int))
print(f_int)

# dictionaries
print('dictionaries')
d1 = {'a':1, 'b':2, 'c':3}
d2 = {'d':4, 'e':5}
d3 = {'k':24, 'm':26}

## join many
func_dict_2 = dict(map(lambda x,y:x+y, d1, d2))
print(func_dict_2)





