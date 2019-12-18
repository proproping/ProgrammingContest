import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
b = list(input())
ans = list()
for i in range(len(b)):
    if b[i] == "A":
        ans.append("T")
    elif b[i] == "T":
        ans.append("A")
    elif b[i] == "C":
        ans.append("G")
    else:
        ans.append("C")
print("".join(ans))
"""

# B
"""
S = input()
ans = 0
count = 0
for i in range(len(S)):
    if S[i] in list("ACGT"):
        count += 1
    else:
        count = 0
    ans = max([ans,count])
print(ans)
"""

# C
import time
st = time.time()
N,Q = map(int,input().split())
S = list(input())
num = list(range(N))
dic1 = dict(zip(num,S))
q = [list(map(lambda x: int(x)-1,input().split())) for _ in range(Q)]
dic2 = {}
for i in range(N-1):
    if dic1[i]+dic1[i+1] == "AC":
        dic2[i] = i
vl = list(dic2.values())
num = list(range(len(vl)))
dic3 = dict(zip(num,vl))
for i in range(Q):
    ans = 0
    for j in range(len(vl)):
        if q[i][0] <= dic3[j] < q[i][1]:
            ans += 1
    print(ans)
print(time.time()-st)
# D


# E


# F
