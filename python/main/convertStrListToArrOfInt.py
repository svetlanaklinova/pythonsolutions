
def convert(strArr):
    return [int(i) for i in strArr if i.isdigit()]


assert convert(['1','3','4']) == [1,3,4]
assert convert(['1','a','4']) == [1,4]