mylist = []
with open('input3.txt') as f:
    mylist = f.read().splitlines()

claiminfo = []
fabric = []
fabric = [[0 for i in range(1000)] for i in range(1000)]

overlap = 0
id_overlaps = set()
id_all = set()


for claim in mylist:
    claiminfo = claim.replace('#', ' ').replace('@',' ').replace(',',' ').replace(':',' ').replace('x', ' ').split()
    id = int(claiminfo[0])
    p2 = int(claiminfo[1])
    p1 = int(claiminfo[2])
    w = int(claiminfo[3])
    h = int(claiminfo[4])
    id_all.add(id)

    for i in range(w):
        if fabric[p1][p2+i] != id and fabric[p1][p2+i] != 0:
            id_overlaps.add(fabric[p1][p2+i])
            fabric[p1][p2+i] = 'X'
            id_overlaps.add(id)
        else:
            fabric[p1][p2+i] = id

        for j in range(h):
            if fabric[p1+j][p2+i] != id and fabric[p1+j][p2+i] != 0:
                id_overlaps.add(fabric[p1+j][p2+i])
                fabric[p1+j][p2+i] = 'X'
                id_overlaps.add(id)

            else:
                fabric[p1+j][p2+i] = id
    
for row in fabric:
    for elem in row:
        if elem == 'X':
            overlap += 1

print('PART 1:' + str(overlap))
print('PART 2:' + str(id_all - id_overlaps))
