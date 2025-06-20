while(True):
    num = int(input())

    if num == -1:
        break

    res =[]

    for i in range(2, num//2+1):
        if num % i == 0:
            res.append(i)

    if sum(res)+1 == num:
        print('{0} = 1 '.format(num), end = '')
        for j in res:
            print('+ {0} '.format(j) ,end = '')
        print()
    else:
        print(f'{num} is NOT perfect.')