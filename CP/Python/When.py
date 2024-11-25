#https://atcoder.jp/contests/abc258/tasks/abc258_a

h=21
m=0
k=int(input())
if k>=60:
    h+=1
    m+=(k-60)
else:
    m+=k
ans=""
if m<10:
    ans=str(h)+":0"+str(m)
else:
    ans=str(h)+":"+str(m)
print(ans)

'''
sample input:
63
output:
22:03
'''
