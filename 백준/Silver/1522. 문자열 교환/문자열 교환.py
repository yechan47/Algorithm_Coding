string = input()
a_cnt = string.count('a')
string += string[0:a_cnt-1]
min_val = 1001

for i in range(len(string)-(a_cnt-1)):
    min_val = min(min_val, string[i:i+a_cnt].count('b'))
print(min_val)