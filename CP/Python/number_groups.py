#https://www.hackerrank.com/challenges/number-groups/problem

import math
import os
import random
import re
import sys

def sumOfGroup(k):
    # Return the sum of the elements of the k'th group.
    n=k+(k-1)**2
    endval=n+(k+(k-1))

    sumodd=0

    for i in range(n,endval,2):
        sumodd+=i
    return sumodd

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    answer = sumOfGroup(k)

    fptr.write(str(answer) + '\n')

    fptr.close()
'''
sample input1:
3
output:
27

sample input2:
4
sample output:
64
'''
