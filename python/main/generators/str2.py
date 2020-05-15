def calculateWays( wordlen , maxvowels):

    #if max vowels = 0 calculating ways

    if maxvowels==0:

        ways = 1

        #loop for calculating ways

        for i in range(wordlen):
            ways = ways*21



        return ways



    else:



        if wordlen == 1: #if word length is 1

            c,v = 1,1

            ways = c * 21 + v * 5 #calculating ways

            return ways

        else: #if max vowels and world length both are greater then 1

            ways = 0

            # patterns with combinations

            for i in range(wordlen):

                c,v = 1,1

                for j in range(wordlen-maxvowels):
                    c = c * 21

                for k in range(maxvowels):
                    v = v * 5

                ways = ways + (v*c) #calculating ways with vowels

            # consonants only

            # ways1 = 1
            ways1 = 21 ** wordlen
            # for i in range(wordlen):
            #     ways1 = ways1*21

            ways = ways + ways1

            # vowels only

            if maxvowels == wordlen:
                ways2 = 5 ** wordlen

                ways = ways + ways2



            return ways # return total ways



print(calculateWays(1, 0))
print(calculateWays(1, 1) )
print(calculateWays(2, 1)) #651
print(calculateWays(2, 2)) #676 ---> output 516
print(calculateWays(4, 2)) #{cccc,vccc,cvcc,ccvc,cccv,vvcc,cvvc,ccvv,vcvc,cvcv}
print(calculateWays(4, 5))