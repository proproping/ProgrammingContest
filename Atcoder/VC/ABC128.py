import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A,P = map(int,input().split())
print((A*3+P)//2)
"""
# B
"""
from operator import itemgetter
N = int(input())
ls = []
for i in range(N):
    s,p = input().split()
    p = int(p)
    ls.append([s,p,i+1])
ls = sorted(ls,key=itemgetter(1),reverse=True)
ls = sorted(ls,key=itemgetter(0))
for i in range(len(ls)):
    print(ls[i][2])
"""
# C
"""
N,M = map(int,input().split())
sw = []
for i in range(M):
    tmp = list(map(int,input().split()))
    sw.append(tmp[1:])
p = list(map(int,input().split()))
bit = []
for i in range(2**N):
    tmp = list(map(int,bin(i)[2:].zfill(N)))
    bit.append(tmp)
ans = 0
for i in range(2**N):
    all = True
    for j in range(M):
        num = 0
        for k in range(len(sw[j])):
            if bit[i][sw[j][k]-1] == 1:
                num += 1
        if num%2 != p[j]:
            all = False
            break
    ans += all
print(ans)
"""
# D
N,K = map(int,input().split())
V = list(map(int,input().split()))
ans = 0
for i in range(min(N,K)+2):
    for j in range(min(N,K)-i):
        print(V[:i])
        print(V[-j-1:])
        if i == 4:
            print("Im fourrrrrrr")
        """
        val = sorted(V[:i+1]+V[-j:])
        while len(val) > 0 and th > 0:
            if val[0] < 0:
                val.pop(0)
                th -= 1
            else:
                break
        if ans < sum(val):
            ans = sum(val)
            """
        

# E


# F
