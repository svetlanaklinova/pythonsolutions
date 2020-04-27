'''
Given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
'''

def maximum69Number (num):
    strNums = list(str(num))
    for index in range(len(strNums)):
        if '6' in strNums[index]:
            strNums[index] = '9'
            break
    return int("".join(strNums))

assert maximum69Number(9669) == 9969
assert maximum69Number(9996) == 9999