import sys
from collections import Counter
from itertools import cycle


mylist = []
with open('input1.txt') as f:
    mylist = f.read().splitlines()

total = 0
sumlist = []
total2 = 0


for num in mylist:
    total += int(num)

print(total)

for num in cycle(mylist):
    total2 += int(num)
    if total2 in sumlist:
        print(total2)
        break
    else:
        sumlist.append(total2)
