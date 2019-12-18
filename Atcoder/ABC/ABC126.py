import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N,K = map(int,input().split())
S = list(input())
S[K-1] = S[K-1].lower()
print("".join(S))
"""

# B
"""
S = input()
tmp1 = int(S[:2])
tmp2 = int(S[2:])
if 0 < tmp1 <= 12 and 0 < tmp2 <= 12:
    print("AMBIGUOUS")
elif (tmp1 == 0 or tmp1 > 12) and 0 < tmp2 <= 12:
    print("YYMM")
elif 0 < tmp1 <= 12 and (tmp2 == 0 or tmp2 > 12):
    print("MMYY")
else:
    print("NA")
"""

# C
"""
N,K = map(int,input().split())
dice = list(range(1,N+1))
count = []
for i in dice:
    tmp = i
    t = 0
    while tmp < K:
        tmp *= 2
        t += 1
    count.append(t)
ans = []
for i in range(len(count)):
    ans.append(1/N*(1/2)**count[i])
print(sum(ans))
"""

# D


# E


# F
