import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,B = map(int,input().split())
tmp = [A,B]
ans = ["Alice","Bob"]
if tmp[0] == tmp[1]:
    print("Draw")
elif tmp[0] == 1:
    print(ans[0])
elif tmp[1] == 1:
    print(ans[1])
elif tmp[0] > tmp[1]:
    print(ans[0])
else:
    print(ans[1])
"""

# B
"""
N,M = map(int,input().split())
A = [input() for i in range(N)]
B = [input() for j in range(M)]
W = len(list(A[0]))-len(list(B[0]))+1
H = N - M + 1
ans = "No"
for i in range(H):
    for j in range(W):
        tmpA = []
        for k in range(M):
             tmpA.append(A[i+k][j:j+len(list(B[0]))])
        if tmpA == B:
            ans = "Yes"
            break
print(ans)
"""

# C


# D


# E


# F
