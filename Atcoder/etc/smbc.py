import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
one = list(map(int,input().split()))
two = list(map(int,input().split()))
if one[0] != two[0]:
    print("1")
else:
    print("0")
"""

# B
"""
import math
N = int(input())
tmp = math.ceil(N/1.08)
if math.floor(tmp*1.08) == N:
    print(int(tmp))
else:
    print(":(")
"""

# C
"""
X = int(input())
tmp = X//100
lis = list(range(tmp*100,tmp*100+5*tmp+1))
if X in lis:
    print(1)
else:
    print(0)
"""

# D
"""
N = int(input())
S = list(input())
pas = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            pas.append(str(i)+str(j)+str(k))
ans = 0
for pw in pas:
    if pw[0] in S:
        ind = S.index(pw[0])
        tmp = S[ind+1:]
    else:
        continue
    if pw[1] in tmp:
        ind = tmp.index(pw[1])
        tmp = tmp[ind+1:]
    else:
        continue
    if pw[2] in tmp:
        ans += 1
print(ans)
"""


# E


# F
