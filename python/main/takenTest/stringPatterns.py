'''
Given the length of a word (wordLen) and the maximum number of consecutive vowels that it can contain (maxVowels), determine how many unique words can be generated.
Words will consist of English alphabetic letters a through z only. Vowels are v: {a, e, i, o, u};
consonants are c: remaining 21 letters. In the explanations, v and c represent vowels and consonants.
'''


def calculateWays(wordLen, maxVowels):
    # prevent entering negative values
    if maxVowels > 5:
        maxVowels = 5
    elif maxVowels < 0:
        maxVowels = 0

    if wordLen < 1 :
        ways = 0
        print("wordLen {}  {}. Total ways: {}".format(wordLen, maxVowels, ways))
        return 0


    # words with only consonants
    ways = 0
    c = 1
    for i in range(wordLen):
        c = c * 21
    ways = ways + c


    if maxVowels:
        if maxVowels == wordLen:
            v = 1
            v = v * 5
            ways = ways + v
        elif (wordLen - maxVowels) > 0 :
            for i in range(wordLen):
                c, v = 1, 1
                for k in range(maxVowels):
                    v = v * 5
                for j in range(wordLen - maxVowels): # combination words: consonants and vowels
                    c = c * 21
                ways = ways + (v * c)

    print("wordLen {} with maxVowels {}. Total ways: {}".format(wordLen, maxVowels, ways))
    return ways


assert calculateWays(-1, -1) == 0
assert calculateWays(0, 0) == 0
assert calculateWays(1, 0) == 21
assert calculateWays(1, 1) == 26
assert calculateWays(4, 0) == 194481
print(calculateWays(4, 1))
print(calculateWays(4, 2))
print(calculateWays(4, 3))
print(calculateWays(4, 5))




