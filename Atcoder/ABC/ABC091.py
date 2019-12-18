import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B,C = map(int,input().split())
if A >= C or B >= C or A+B >= C:
    print("Yes")
else:
    print("No")
"""

# B
"""
N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for j in range(M)]
x = list(set(s))
def counter(x,N,s,M,t):
    ans = [0]
    for i in range(len(x)):
        tmp = 0
        for j in range(N):
            if x[i] == s[j]:
                tmp += 1
        for k in range(M):
            if x[i] == t[k]:
                tmp += (-1)
        ans.append(tmp)
    return(ans)
print(max(counter(x,N,s,M,t)))
"""

# C


# D


# E


# F
