



def check(sourceStr):
    if not sourceStr or len(sourceStr) == 0:
        return False

    open = ["(", "[", "{"]
    close = [")", "]","}"]

    st = []

    for el in sourceStr:
        if el in close:
            pos = close.index(el)
            if st:
                last = st[-1]
                if open[pos] == last:
                    st.remove(last)
                else:
                    return False
            continue
        if el in open:
            st.append(el)

    if len(st) == 0:
        return True

    return False


assert(check("[[[]]]") == True)
assert(check("[[ [   ]]]") == True)
assert(check("[[sdg [  gdad ]]]") == True)
assert(check("") == False)
assert(check("[[ [  ) ]]]") == False)
assert(check("[[ [  ) ]asdfjdljt]") == False)