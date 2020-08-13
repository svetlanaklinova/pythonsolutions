from itertools import chain, combinations, product


#dt =  [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
# d_max_size = len(dt) + 1
# lst = set(list(combinations(dt, 3)))
# print(lst)

str_input = 'sdgk'

dict = {'a':1, 'b':'gasa'}
def generate(inp):
    result = list(
        chain(
            list(
                set(
                    combinations(inp,r)
                ) for r in range(len(inp) + 1)
            )
        )
    )
    return result




#print(generate(dt))
print(generate(str_input))

