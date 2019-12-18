import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
import datetime
S = list(map(int,input().split("/")))
tmp = datetime.date(S[0],S[1],S[2])
if tmp <= datetime.date(2019,4,30):
    print("Heisei")
else:
    print("TBD")
"""

# B
"""
N = int(input())
matrix = [input().split() for i in range(N)]
ans = 0
for i in range(N):
    if matrix[i][1] == "JPY":
        ans += float(matrix[i][0])
    else:
        ans += float(matrix[i][0])*float(380000.0)
print(ans)
"""

# C


# D


# E


# F
