from array import *

mylist = []
with open('input3.txt') as f:
    mylist = f.read().splitlines()

claiminfo = []
fabric = [[],[]]


for claim in mylist:
    claiminfo = claim.replace('@',' ').replace(':',' ').split()
    fabric[1].append(4)
    print(fabric)
    # fabric[int(claiminfo[1][0])].append(1)
    
# fabric[0].append(1)
# print(fabric)

# for row in fabric:
#     fabric[row].append(1)
#     print(fabric)
#     for element in row:
#         print('done')