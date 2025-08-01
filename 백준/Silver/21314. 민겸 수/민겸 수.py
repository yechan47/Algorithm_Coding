n = input()
m = 0
max_val = ''
min_val = ''
cnt = 0
for i in n:
    if i == 'K':
        if m > 0:
            max_val += str(5 * 10 ** m)
            min_val += str(1 * 10 ** m + 5)
            m = 0
        else: 
            max_val += '5'
            min_val += '5'

    else:
        m += 1
if m > 0: 
    max_val += '1' * (m)
    min_val += str(1*10**(m-1))
print(max_val)
print(min_val)