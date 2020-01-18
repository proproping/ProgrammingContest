import sys
import os
f = open('input.txt','r')
sys.stdin = f

"A"
"""
import math
H = int(input())
W = int(input())
N = int(input())
which = max(H,W)
print(math.ceil(N/which))
"""

"B"
"""
from operator import itemgetter
N = int(input())
q = []
ans = 0
for i in range(N):
    x,l = map(int,input().split())
    q.append([x-l,x+l])
q = sorted(q,key = itemgetter(1))
last = -10**18
for i in range(N):
    tmp = q[i]
    if tmp[0] >= last:
        ans += 1
        last = tmp[1]
print(ans)
"""

"C"
"""
N,K,S = map(int,input().split())
if S == 10**9:
    ans = [S]*K+[S-1]*(N-K)
    print(*ans,sep = " ")
else:
    ans = [S]*K+[S+1]*(N-K)
    print(*ans,sep = " ")
"""

"D"
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
flag = False
ans = 0
count = 0
while True:
    if count == 10**5:
        ans = -1
        break
    for i in range(1,N):
        if A[i-1] > A[i]:
            break
        if i == N-1:
            flag = True
    if flag:
        break
    for i in range(1,N):
        if B[i-1] > B[i] or A[i-1] > A[i]:
            tmpA = [A[i-1],A[i]]
            tmpB = [B[i-1],B[i]]
            A[i-1],A[i] = tmpB[1],tmpB[0]
            B[i-1],B[i] = tmpA[1],tmpA[0]
            ans += 1
    count += 1
print(ans)


"E"


"F"

