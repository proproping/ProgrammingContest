import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = int(input())
A = int(input())
if N%500 > A:
    print("No")
else:
    print("Yes")
"""

# B
"""
N = int(input())
a = list(map(int,input().split()))
if len(a)%2 != 0:
    a.append(0)
    N += 1
alice = []
bob = []
for i in range(int(N/2)):
    alice.append(a.pop(a.index(max(a))))
    bob.append(a.pop(a.index(max(a))))
print(sum(alice)-sum(bob))
"""

# C
"""
c = [list(map(int,input().split())) for _ in range(3)]
a = [0]*3
b = c[0]
a[1] = c[1][0]-b[0]
a[2] = c[2][0]-b[0]
flag = False
ans = "Yes"
for i in range(3):
    if flag:
        break
    for j in range(3):
        if c[i][j] != a[i]+b[j]:
            ans = "No"
            flag = True
            break
print(ans)
"""
# D


# E


# F
