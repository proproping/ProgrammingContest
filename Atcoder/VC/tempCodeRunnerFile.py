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
N = int(input())
P = [int(input()) for _ in range(N)]
count = 1
flag = ""
for i in range(1,N):
    if flag == "":
        if P[i-1] < P[i]:
            flag = "<"
        else:
            flag = ">"
    else:
        if (P[i-1] < P[i] and flag == "<") or (P[i-1] > P[i] and flag == ">"):
            continue
        else:
            count += 1
            if P[i-1] < P[i]:
                flag = "<"
            else:
                flag = ">"
print(count)

"C"


"D"


"E"


"F"


