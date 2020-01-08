import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
a,b,c = map(int,input().split())
if (b-a) == (c-b):
    print("YES")
else:
    print("NO")
"""

# B
"""
O = input()
E = input()
ans = []
for i in range(len(list(E))):
    ans.append(O[i])
    ans.append(E[i])
if len(list(O)) != len(list(E)):
    ans.append(O[-1])
print("".join(ans))
"""

# C
"""
import collections
n = int(input())
S = [input() for _ in range(n)]
abc = list("abcdefghijklmnopqrstuvwxyz")
dic = dict(zip(abc,[10**9]*len(abc)))
for i in range(n):
    tmp = collections.Counter(list(S[i]))
    for j in abc:
        if dic[j] > tmp[j]:
            dic[j] = tmp[j]
ans = []
for k in abc:
    for l in range(dic[k]):
        ans.append(k)
print(*ans,sep="")
"""

# D


# E


# F
