def weather_caster():
    arr = list(input())
    cloud = False
    move_cnt = 0
    ans = []
    for s in arr:
        if s == 'c':
            ans.append(0)
            move_cnt = 1
            cloud = True
        elif cloud and s == '.':
            ans.append(move_cnt)
            move_cnt += 1
        else:
            ans.append(-1)

    return " ".join(map(str, ans))


h, w = map(int, input().split())
for _ in range(h):
    print(weather_caster())