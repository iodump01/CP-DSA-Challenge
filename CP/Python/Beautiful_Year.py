#https://codeforces.com/problemset/problem/271/A

a=int(input())

for i in range(a+1,9999):
    s=str(i)
    b=set(s)
    if len(b)==len(s):
        print(i)
        break
    else:
        continue

'''
Sample input:
1987
output:
2013
'''
