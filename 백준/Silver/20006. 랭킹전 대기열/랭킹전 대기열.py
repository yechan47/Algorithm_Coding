player, room_max = map(int, input().split())
room_list=[]
level, nick = input().split()
level = int(level)
room_list.append([[level, nick]])

try:
    while True:
        success = 0
        level, nick = input().split()
        level = int(level)
        for i in room_list:
            if level <= i[0][0] + 10 and level >= i[0][0] - 10 and len(i) < room_max:
                i.append([level, nick])
                success = 1
                break
        if success == 0:
            room_list.append([[level, nick]])
except EOFError:
    pass

for i in range(len(room_list)):
    room_list[i] = sorted(room_list[i], key = lambda x: (x[1],x[0]))

for i in room_list:
    if len(i) == room_max:
        print('Started!')
    else:
        print('Waiting!')
    for j in i:
        print(j[0], j[1])