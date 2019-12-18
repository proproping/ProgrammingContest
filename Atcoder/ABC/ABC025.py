import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
S = input()
N = int(input())
tmp = []
for i in range(5):
    for j in range(5):
        tmp.append(S[i]+S[j])
print(tmp[N-1])
"""

# B
"""
N,A,B = map(int,input().split())
mat = [input().split() for i in range(N)]
for i in range(N):
    if int(mat[i][1]) < A:
        mat[i][1] = A
    elif int(mat[i][1]) > B:
        mat[i][1] = B
    if mat[i][0] == "West":
        mat[i][1] = int(mat[i][1]) * (-1)
    elif mat[i][0] == "East":
        mat[i][1] = int(mat[i][1])
ans = 0
for i in range(len(mat)):
    ans += mat[i][1]
if ans > 0:
    print("East "+str(abs(ans)))
elif ans < 0:
    print("West "+str(abs(ans)))
else:
    print(ans)
"""

# C


# D


# E


# F
