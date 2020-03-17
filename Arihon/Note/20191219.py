import sys
import os
f = open('input.txt','r')
sys.stdin = f

class BIT():
    def __init__(self,n):
        self.dat = [0]*(n+1)

    def add(self,a,x):
        i = a
        while i < len(self.dat):
            self.dat[i] = self.dat[i] + x
            i += i & -i

    def sum(self,a):
        res = 0
        i = a
        while i > 0:
            res += self.dat[i]
            i -= i & -i
        return res

n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
tmp = BIT(n)
dic = {}
for i in range(len(b)):
    dic[b[i]] = i+1

ans = 0
for j in range(n):
    ans += j - tmp.sum(dic[a[j]])
    tmp.add(dic[a[j]],1)
print(ans)
