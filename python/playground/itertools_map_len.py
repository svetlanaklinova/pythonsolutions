
'''
format of usage:
- for strings
result = output_data_type(map(len, input_data_type))

- for numbers and combinations
result = output_data_type(map(lambda x : len(str(x)), input_data_type)
'''

# count length of each value in list
## strings
str_l = ['abc', 'dgsfd', 'gstewe']
str_len = list(map(len, str_l))
print(str_len) # [3, 5, 6]

## integeres
int_l = [1,23,456,7890]
int_len = list(map(lambda x : len(str(x)), int_l))
print(int_len) # [1, 2, 3, 4]

## tuples
tup_l = (23, 'sghsegs', 'gs89')
tup_len = tuple(map(lambda x : len(str(x)), tup_l))
print(tup_len) #(2, 7, 4)




