import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
b = list(input())
ans = list()
for i in range(len(b)):
    if b[i] == "A":
        ans.append("T")
    elif b[i] == "T":
        ans.append("A")
    elif b[i] == "C":
        ans.append("G")
    else:
        ans.append("C")
print("".join(ans))
"""

# B
"""
S = input()
ans = 0
count = 0
for i in range(len(S)):
    if S[i] in list("ACGT"):
        count += 1
    else:
        count = 0
    ans = max([ans,count])
print(ans)
"""

# C
"""
N,Q = map(int,input().split())
S = input()
ac = [0]*(N+1)
for i in range(N):
    ac[i+1] = ac[i] + (1 if S[i:i+2] == "AC" else 0)
for i in range(Q):
    l,r = map(int,input().split())
    print(ac[r-1]-ac[l-1])
"""

# D


# E


# F
