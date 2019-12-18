import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
X,t = map(int,input().split())
if X < t:
    print(0)
else:
    print(X-t)
"""


# B
"""
s = input()
tmp = list(range(0,len(s),2))
ans = []
for i in tmp:
    ans.append(s[i])
print("".join(ans))
"""

# C
"""
N = int(input())
a = list(map(int,input().split()))
num = list(range(10**5+1))
val = [0]*(10**5+1)
dic = dict(zip(num,val))
for i in a:
    if i == 0:
        dic[i] += 1
        dic[i+1] += 1
    elif i == 10**5:
        dic[i-1] += 1
        dic[i] += 1
    else:
        dic[i-1] += 1
        dic[i] += 1
        dic[i+1] += 1
print(max(dic.values()))
"""

# D


# E


# F
