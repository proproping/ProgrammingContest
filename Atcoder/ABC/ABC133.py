import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
n,a,b = map(int, input().split())
print(min(a*n,b))
"""

# B
"""
from itertools import combinations
import numpy as np
N,D = map(int,input().split())
X = []
for i in range(N):
    X.append(np.array(list(map(int,input().split()))))
comb = list(combinations(list(range(N)),2))
count = 0
for i in range(len(comb)):
    dist = (sum(list(np.power(X[comb[i][0]]-X[comb[i][1]],2))))**(1/2)
    if int(dist) == dist:
        count += 1
print(count)
"""

# C

L,R = map(int,input().split())
if R - L > 2019:
        print(0)
else:
    ans = 10**9
    for i in range(L,R):
        for j in range(i+1,R+1):
            if ans > i*j%2019:
                ans = i*j%2019
                if ans == 0:
                    break
    print(ans)


# D


# E


# F
