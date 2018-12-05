import collections

mylist = []
with open('input4.txt') as f:
    mylist = f.read().splitlines()

#josh gave me this
mylist.sort(key = lambda l: l.split("[")[1].split("]")[0])
#sorted : (

current_id = 0

wake_time = 0
sleep_time = 0

guards = {}
min_list = []

for log in mylist:
    if '#' in log:
        id = int(log[log.find('#') : log.find('b')].replace('#', ''))

    else:
        if 'f' in log:
            sleep_time = int(log[log.find(':') + 1 : log.find(']')])
        if 'w' in log:
            wake_time = int(log[log.find(':') + 1 : log.find(']')])
            min_asleep = wake_time - sleep_time

            if guards.get(id) is None:
                guards[id] = 0
            if guards.get(id) is not None :
                y = guards.get(id)
                x = y + min_asleep
                guards[id] = x

print('MAX: ' + str(max(guards.values())))
maximum_value = max(guards.values())

def find_key(input, value):
    for id, sleep in input.items():
        if sleep == value:
            return id

chosen_guard = find_key(guards, maximum_value)

print('GUARD ID: ' + str(find_key(guards, maximum_value)))

for log in mylist:
    if '#' in log:
        id = int(log[log.find('#') : log.find('b')].replace('#', ''))

    else:
        if 'f' in log:
            sleep_time = int(log[log.find(':') + 1 : log.find(']')])
        if 'w' in log:
            wake_time = int(log[log.find(':') + 1 : log.find(']')])
            min_asleep = wake_time - sleep_time

            if id == chosen_guard:
                for min in range(sleep_time, wake_time):
                    min_list.append(min)

c = collections.Counter(min_list).most_common(1)
print('MOST SLEPT MINUTE: ' + str(c[0][0])) 
answer = int(c[0][0]) * int(chosen_guard)
print('PART 1: ' + str(answer))
