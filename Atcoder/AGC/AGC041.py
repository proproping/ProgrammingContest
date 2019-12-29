import sys
import os
f = open('input.txt','r')
sys.stdin = f

"A"
"""
N,A,B = map(int,input().split())
if (A-B)%2 == 0:
    print(abs((A-B)//2))
elif A == 1 or B == N:
    print((abs(A-B)-1)//2+1)
else:
    which = min((A-1),N-B)
    if which == A-1:
        count = A-1+1
        A = 1
        B -= count
        print(abs(A-B)//2+count)
    else:
        count = N-B+1
        A += count
        B = N
        print(abs(A-B)//2+count)
"""

"B"
N,M,V,P = map(int,input().split())
A = sorted(list(map(int,input().split())))
seta = list(set(A))
count = 0
tmp = -P+(V)
if tmp > 0:
    tmp = -1
for i in range(N):
    if A[i]+M >= A[-1]:
        count += 1
print(count)