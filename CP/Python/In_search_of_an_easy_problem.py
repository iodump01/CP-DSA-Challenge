#https://codeforces.com/problemset/problem/1030/A

n=int(input())
arr=list(map(int,input().split()))
if sum(arr)==0:
    print("EASY")
else:
    print("HARD")

'''
sample input:
3
0 0 1
output:
HARD
'''
