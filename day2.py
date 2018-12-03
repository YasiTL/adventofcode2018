import sys
import collections

mylist = []
with open('input2.txt') as f:
    mylist = f.read().splitlines()
    
doubleletter = 0
trippleletter = 0

for code in mylist:
    nodouble = True
    notripple = True
    for letter in code:
        freq = code.count(letter)
        if freq == 2 and nodouble:
            doubleletter += 1
            nodouble = False
        if freq == 3 and notripple:
            trippleletter += 1
            notripple = False

print('PART 1: '+ str(doubleletter*trippleletter))

# my clever plan didnt work :(

# for code in mylist:
#     for code2 in mylist:
#         s1 = set(code)
#         s2 = set(code2)
#         resultset = s1 - s2
#         if len(resultset) == 1:
#             print(list(resultset))
#             # print(''.join(resultlist))

for code in mylist:
    for code2 in mylist:
        difference = 0
        for i in range(len(code)):
            if code[i] != code2[i]:
                difference += 1
        if difference == 1:
            answer = []
            for i in range(len(code)):
                if code[i] == code2[i]:
                    answer.append(code[i])
            print('PART 2: ' + ''.join(answer))
