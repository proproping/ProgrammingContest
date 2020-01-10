import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
A = int(input())
B = int(input())
C = int(input())
D = int(input())
print(min([A,B])+min([C,D]))
"""

# B
"""
N = int(input())
D,X = map(int,input().split())
A = [int(input()) for i in range(N)]
count = N
for i in range(N):
    tmp = A[i]
    while (A[i]+1) <= D:
        count += 1
        A[i] += tmp
print(count+X)
"""

# C
"""
N = int(input())
A = list(map(int,input().split()))
A.insert(0,0),A.append(0)
time = 0
now = 0
for i in range(N+2):
    time += abs(A[i]-now)
    now = A[i]
for i in range(1,N+1):
    if A[i-1] <= A[i] <= A[i+1]:
        print(time)
    else:
        print(time-((abs(A[i-1]-A[i])+abs(A[i]-A[i+1]))-abs(A[i-1]-A[i+1])))
"""
# D


# E


# F
