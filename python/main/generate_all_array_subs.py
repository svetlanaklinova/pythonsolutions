''' Print all sub sets of array'''

def getAllSubArrays(ar):
    temp = []
    gen = []

    size = len(ar)

    for startPoint in range(size +1):
        for groupSize in range(startPoint, size + 1):
            for i in range(startPoint, groupSize):
                num = ar[i]
                if num not in temp:
                    temp.append(ar[i])
            if temp not in gen:
                gen.append(temp)
            temp = []
    mis = [ar[0], ar[size-1]]
    if mis not in gen:
        gen.append(mis)
    return gen




print(getAllSubArrays([1,2,3]))