import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
S = input()
count = 0
for i in range(3):
    if S[i] == "1":
        count += 1
print(count)
"""

# B
"""
N = int(input())
A = list(map(int,input().split()))
flag = 1
while flag == 1:
    for i in range(N):
        if A[i]%2 != 0:
            flag = 0
            break
"""

# C
"""
N,K = map(int,input().split())
A = list(map(int,input().split()))
species = list(set(A))
dic = {}
for i in species:
    dic[i] = 0
for i in A:
    dic[i] += 1
if K >= len(species):
    print(0)
else:
    tmp = sorted(dic.values(),reverse=1)
    print(sum(tmp[K:]))
"""

# D


# E


# F
