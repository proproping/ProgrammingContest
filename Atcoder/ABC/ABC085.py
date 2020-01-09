import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
S = input()
tmp = list(S)
tmp[3] = "8"
print("".join(tmp))
"""

# B
"""
N = int(input())
d = set([int(input()) for i in range(N)])
print(len(d))
"""

# C
"""
N,Y = map(int,input().split())
A,B,C = -1,-1,-1
flag = False
for i in range(N+1):
    if flag:
        break
    for j in range(N+1-i):
        if i*10000 + j*5000 + (N-i-j)*1000 == Y and (N-i-j) >= 0:
            A,B,C = i,j,(N-i-j)
            flag = True
            break
print(A,B,C)
"""
# D


# E


# F
"""
10000
10
6
2
1

5000
1
5

1000
1
"""