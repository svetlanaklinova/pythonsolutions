

def rever(x):
    div = 1
    sX = str(x)

    if str(sX).startswith("-"):
        div = -1
        sX = sX[1:]

    result = sX[::-1]
    return int(result) // div

n = -240
assert(rever(-240) == -42)
assert(rever(100) == 1)