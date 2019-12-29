import sys
import os
f = open('input.txt','r')
sys.stdin = f

#A
"""
S,T = map(str,input().split())
print(T+S)
"""
#B
"""
A,B,K = map(int,input().split())
if K <= A:
    print(A-K,B)
else:
    print(0,max(0,B-(K-A)))
"""
#C
"""
X = int(input())
ans = 0
def isPrime(n):
    i = 2
    while i**2 <= n:
        if n%i == 0:
            return False
        i += 1
    return n != 1
while ans == 0:
    if isPrime(X):
        ans = X
    else:
        X += 1
print(ans)
"""

#D
"""
N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(input())
for i in range(N-K):
    if T[i] == T[i+K]:
        T[i+K] = "@"
dic1 = {"r":P,"s":R,"p":S,"@":0}
points = 0
for i in range(N):
    points += dic1[T[i]]
print(points)
"""

#E
"""
N,M = map(int,input().split())
A = sorted(list(map(int,input().split())),reverse=1)
ans = 0
if M >= (N**2//2):
    ans = sum(A)*2*N
    for i in range((N**2-M)):
        ans -= 0
else:
    for i in range(M):
        ans += 0
print(ans)
"""

#F