
total_vowels = 5
total_consonants = 21

def single_pair():
    global total_consonants,total_vowels
    ways = 0
    ways = ways + total_consonants
    return ways + total_vowels


def consonants_only(wordlen):
    global total_consonants
    return total_consonants**wordlen

def vowels_only(maxvowels):
    global total_vowels
    return total_vowels**maxvowels


def calculatePossibilities(wordlen, maxvowels):

    ways = 0
    if not wordlen or maxvowels > wordlen:
        return 0


    if maxvowels == 0:
         ways = consonants_only(wordlen)

    elif wordlen == maxvowels:
          ways = single_pair() ** wordlen

    elif maxvowels < wordlen:
        # consonants only
           ways = consonants_only(wordlen)

                #combinations
           consonants_in_combination = wordlen - maxvowels
           s_combination = vowels_only(maxvowels) * consonants_only(consonants_in_combination)

           for i in range(wordlen):
               ways = ways + s_combination



    print(f'wordlen {wordlen} vowels {maxvowels}, result {ways}')
    return ways

### Test ######
expected = 21
actual = calculatePossibilities(1, 0)
print(f'expected {expected}, actual {actual}')
assert actual == expected #{c} 21

expected = 21 + 5
actual = calculatePossibilities(1, 1)
print(f'expected {expected}, actual {actual}')
assert calculatePossibilities(1, 1) == expected #{c,v} 21 + 5

expected = 5*5 + 21*21 + 21*5 + 5*21 #676
actual = calculatePossibilities(2, 2)
print(f'expected {expected}, actual {actual}')
assert actual == expected  #{vv,cc,cv,vc} 5*5 + 21*21 + 21*5 + 5*21

expected = 21*21 + 21*5 + 5*21 #651
actual = calculatePossibilities(2, 1) #{vc,cv,cc}
print(f'expected {expected}, actual {actual}')
assert actual == expected


expected = 21**4 + 21*21*21*5 + 21*21*5*21 + 21*5*21*21 + 5*21*21*21 #379701
actual = calculatePossibilities(4, 1) #{cccc,cccv,ccvc,cvcc,vccc}
print(f'expected {expected}, actual {actual}')
assert actual == expected

                                                          #
expected = 21*21*21*21 #194481
actual = calculatePossibilities(4, 0) #{cccc}
print(f'expected {expected}, actual {actual}')
assert actual == expected


