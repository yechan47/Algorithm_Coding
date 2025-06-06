for i in range(int(input())):
    s=sorted(list(map(int,input().split())))
    print('Scenario #{}:'.format(i+1))
    if s[0]**2 + s[1]**2 == s[2]**2:  
        print("yes\n")
    else:
        print("no\n")