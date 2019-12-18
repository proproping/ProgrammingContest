import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
N = input()
if "9" in N:
    print("Yes")
else:
    print("No")
"""

# B
"""
N = int(input())
mat = [list(map(int,input().split())) for i in range(N)]
ans = 0
for i in range(len(mat)):
    ans += len(list(range(mat[i])))
print(ans)
"""

# C
"""
N = int(input())
A = [int(input()) for i in range(N)]
keys = list(set(A))
values = [0]*len(keys)
dic = {}
dic.update(zip(keys,values))
for i in A:
    dic[i] += 1
tmp = [i%2 for i in dic.values()]
print(sum(tmp))
"""

# D


# E


# F
