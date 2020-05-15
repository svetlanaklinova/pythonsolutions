'''
Modify list as expected and print:
Set = {'G4','G3','R1','R4','G2','G5','R2','G1','R3','R5'}
output = ['R1', 'R2', 'R3', 'R4', 'R5', 'G1', 'G2', 'G3', 'G4', 'G5']
'''
Set = {'G4','G3','R1','R4','G2','G5','R2','G1','R3','R5'}
def sol1():
    global Set

    r = sorted([x for x in Set if x.startswith('R')])
    g = sorted([x for x in Set if x.startswith('G')])



    print(r+g)

# def sol2():
#     global set
#     size = len(set)
#     nl = []
#     while size:
#         for card in set:
#             if card.startswith('G'):
#                 nl.append(card)
#             else:
#                 nl.insert(0,card)
#         size = size -1

sol1()



