#https://codeforces.com/problemset/problem/1535/A
t=int(input())
for i in range(t):
    arr=list(map(int,input().split()))
    n=len(arr)
    max1=max(arr[0],arr[1])
    max2=max(arr[2],arr[3])
    arr.sort()
    m1=arr[n-1]
    m2=arr[n-2]
    if (max1==m1 or max1==m2) and (max2==m1 or max2==m2):
        print("YES")
    else:
        print("NO")

'''
sample input1:
4
4
3 7 9 5
4 5 6 9
5 3 8 1
6 5 3 2

ouput1:
YES
NO
YES
NO
'''
