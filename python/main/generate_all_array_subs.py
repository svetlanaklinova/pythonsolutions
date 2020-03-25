''' Print all sub sets of array'''

def getAllSubArrays(ar):
    temp = []
    gen = []

    size = len(ar)

    for startPoint in range(size):
        for groupSize in range(startPoint, size + 1):
            for i in range(startPoint, groupSize):
                num = ar[i]
                if num not in temp:
                    temp.append(ar[i])
            if temp:
                gen.append(temp)
            temp = []
    print(gen)



print(getAllSubArrays([1,2,3]))