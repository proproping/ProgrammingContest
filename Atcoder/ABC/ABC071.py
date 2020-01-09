import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
x,a,b = map(int,input().split())
if abs(x-a) > abs(x-b):
    print("B")
else:
    print("A")
"""

# B
"""
S = input()
tmp = list("abcdefghijklmnopqrstuvwxyz")
ans = []
for i in range(len(tmp)):
    if tmp[i] not in S:
        ans.append(tmp[i])
if len(ans) == 0:
    print("None")
else:
    print(ans[0])
"""

# C
"""
from collections import Counter
N = int(input())
A = list(map(int,input().split()))
count = Counter(A)
A = sorted(list(set(A)),reverse = True)
a,b = 0,0
for i in A:
    if a == 0:
        if count[i] >= 4:
            a,b = i,i
            break
        elif count[i] >= 2:
            a = i
    else:
        if count[i] >= 2:
            b = i
            break
print(a*b)
"""
# D


# E


# F
