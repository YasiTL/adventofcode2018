mylist = []
with open('input3.txt') as f:
    mylist = f.read().splitlines()

claiminfo = []
fabric = []
fabric = [[0 for i in range(1000)] for i in range(1000)]

overlap = 0
idoverlaps = set()
ids = set()


for claim in mylist:
    claiminfo = claim.replace('#', ' ').replace('@',' ').replace(',',' ').replace(':',' ').replace('x', ' ').split()
    id = int(claiminfo[0])
    p2 = int(claiminfo[1])
    p1 = int(claiminfo[2])
    w = int(claiminfo[3])
    h = int(claiminfo[4])
    ids.add(id)

    for i in range(w):
        if fabric[p1][p2+i] != id and fabric[p1][p2+i] != 0:
            idoverlaps.add(fabric[p1][p2+i])
            fabric[p1][p2+i] = id
            idoverlaps.add(id)
        else:
            fabric[p1][p2+i] = id

        for j in range(h):
            if fabric[p1+j][p2+i] != id and fabric[p1+j][p2+i] != 0:
                idoverlaps.add(fabric[p1+j][p2+i])
                fabric[p1+j][p2+i] = id
                idoverlaps.add(id)

            else:
                fabric[p1+j][p2+i] = id
    


for row in fabric:
    for elem in row:
        if elem == 'X':
            overlap += 1

print(overlap)
print(len(ids))
print('PART 2:' + str(ids-idoverlaps))
