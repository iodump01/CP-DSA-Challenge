#https://codeforces.com/problemset/problem/758/A

n=int(input())
arr=list(map(int,input().split()))
if n==1:
    print(0)
else:
    sumof=0
    arr.sort()
    max=arr[n-1]
    for i in range(n-1):
        sumof+=max-arr[i]
    print(sumof)

'''
sample input1:
5
0 1 2 3 4
output1:
10

sample input2:
3
1 3 1
output2:
4
'''
