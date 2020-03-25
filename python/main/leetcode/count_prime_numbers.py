

def countPrimes( n):

    result = []
    for i in range(n ):
        if isPrime(i):
                result.append(i)
    resLen = len(result)
    print('Detected {0} prime(s): {1}'.format(resLen,result))
    return resLen

def isPrime(num):
    if num <=1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True



assert (countPrimes(2) == 0)
assert (countPrimes(3) == 1)
assert (countPrimes(7) == 3)