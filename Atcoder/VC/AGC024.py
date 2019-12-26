import sys
import os
f = open('input.txt','r')
sys.stdin = f

"A"
"""
A,B,C,K = map(int,input().split())
if abs(A-B) > 10**18:
    print("Unfair")
else:
    print((A-B)*(-1)**(K))
"""
"B"
"""
N = int(input())
P = []
indexls = [0]*N
for i in range(N):
    tmp = int(input())
    P.append(tmp)
    indexls[tmp-1] = i
maxlen = 1
tmplen = 1
for i in range(1,N):
    if indexls[i] > indexls[i-1]:
        tmplen += 1
        maxlen = max(maxlen,tmplen)
    else:
        tmplen = 1
print(N-maxlen)
"""
"C"
"""
N = int(input())
A = [int(input()) for _ in range(N)]
"""

"D"


"E"


"F"


