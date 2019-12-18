import sys
import os
f = open('input.txt', 'r')
sys.stdin = f

# A
"""
S = input()
dic = {"SAT":1,"FRI":2,"THU":3,"WED":4,"TUE":5,"MON":6,"SUN":7}
print(dic[S])
"""

# B
"""
N = int(input())
S = list(input())
al = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
dic1 = dict(zip(al,list(range(len(al)))))
tmp = []
for i in S:
    tmp.append((dic1[i]+N)%26)
dic2 = dict(zip(list(range(len(al))),al))
ans = []
for j in tmp:
    ans.append(dic2[j])
print(*ans,sep="")
"""

# C
"""
import math
A,B,X = map(int,input().split())
N = 1
if A*N+B >= X:
    print(0)
else:
    N = math.ceil(X/A)
    N = math.ceil(N - (B/A)*len(str(N)))
    if A*N + B*(len(list(str(N)))) > X:
        while A*N + B*(len(list(str(N)))) > X:
            N += -1
        if N > 10**9:
            print(10**9)
        else:
            print(N)
    else:
        while A*N + B*(len(list(str(N)))) < X:
            N += 10**9
        while A*N + B*(len(list(str(N)))) > X:
            N += -10**9
        while A*N + B*(len(list(str(N)))) < X:
            N += 10**8
        while A*N + B*(len(list(str(N)))) > X:
            N += -10**8
        while A*N + B*(len(list(str(N)))) < X:
            N += 10**7
        while A*N + B*(len(list(str(N)))) > X:
            N += -10**7
        while A*N + B*(len(list(str(N)))) < X:
            N += 10**6
        while A*N + B*(len(list(str(N)))) > X:
            N += -10**6
        while A*N + B*(len(list(str(N)))) < X:
            N += 10**5
        while A*N + B*(len(list(str(N)))) > X:
            N += -10**5
        while A*N + B*(len(list(str(N)))) < X:
            N += 10**4
        while A*N + B*(len(list(str(N)))) > X:
            N += -10**4
        while A*N + B*(len(list(str(N)))) < X:
            N += 10**3
        while A*N + B*(len(list(str(N)))) > X:
            N += -10**3
        while A*N + B*(len(list(str(N)))) < X:
            N += 10**2
        while A*N + B*(len(list(str(N)))) > X:
            N += -10**2
        while A*N + B*(len(list(str(N)))) < X:
            N += 10**1
        while A*N + B*(len(list(str(N)))) > X:
            N += -10**1
        while A*N + B*(len(list(str(N)))) < X:
            N += 10**0
        while A*N + B*(len(list(str(N)))) > X:
            N += -10**0
        if N > 10**9:
            print(10**9)
        else:
            print(N)
"""

# D
"""
N = int(input())
mat = [list(map(int,input().split())) for i in range(N-1)]
dic = dict(zip(range(1,N+1),[0]*N))
for i in range(N-1):
    for j in range(2):
        dic[mat[i][j]] += 1
K = max(dic.values())
index = max(dic.items(),key = lambda x:x[1])[0]
save = [[] for i in range(N)]
tmp = [0]*(N-1)
num = 1
for i in range(N-1):
    if index in mat[i]:
        tmp[i] = num
        save[mat[i][0]-1].append(num)
        save[mat[i][1]-1].append(num)
        num += 1
if 0 not in tmp:
    print(K)
    for i in range(len(tmp)):
        print(tmp[i])
else:
    for i in range(len(tmp)):
        if tmp[i] == 0:
            for j in range(1,K+1):
                if j not in save[mat[i][0]-1] and j not in save[mat[i][1]-1]:
                    tmp[i] = j
                    save[mat[i][0]-1].append(j)
                    save[mat[i][1]-1].append(j)
    print(K)
    for k in range(len(tmp)):
        print(tmp[i])
"""

# E


# F
