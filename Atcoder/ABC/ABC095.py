import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
S = input()
ans = 700
for i in range(3):
    if S[i] == "o":
        ans += 100
print(ans)
"""

# B
"""
N,X = map(int,input().split())
m = [int(input()) for i in range(N)]
ans = len(m)
f = X - sum(m)
ans += f//min(m)
print(ans)
"""

# C
"""
A,B,C,X,Y = map(int,input().split())
if A > 2*C and B > 2*C:
    print(2*max([X,Y])*C)
elif A > 2*C:
    if X > Y:
        print(2*C*X)
    else:
        print(2*C*X+B*(Y-X))
elif B > 2*C:
    if X > Y:
        print(A*(X-Y)+2*C*Y)
    else:
        print(2*C*Y)
elif A+B > 2*C:
    if X > Y:
        print(2*min([X,Y])*C + abs(X-Y)*A)
    else:
        print(2*min([X,Y])*C + abs(X-Y)*B)
else:
    print(A*X+B*Y)
"""

# D


# E


# F
