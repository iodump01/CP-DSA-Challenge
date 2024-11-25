#https://atcoder.jp/contests/abc263/tasks/abc263_a

n=5
arr=list(map(int,input().split()))
brr=set(arr)
if len(brr)==2 and (arr.count(arr[0])==2 or arr.count(arr[0])==3 ):
    print("Yes")
else:
    print("No")

'''
sample input1:
1 1 1 2 2
output:
Yes

sample input2:
1 2 3 1 1
ouput:
No
'''
