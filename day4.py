mylist = []
with open('input4.txt') as f:
    mylist = f.read().splitlines()

#josh gave me this
mylist.sort(key = lambda l: l.split("[")[1].split("]")[0])

for log in mylist:
    print(log[log.find('#') + 1 : log.find('b')])