import math
def isPrime(n):
    i = 2
    while i**2 <= n:
        if n%i == 0:
            return False
        i += 1
    return n != 1
def main():
    t = int(input())
    for i in range(t):
        a,b,c = 0,0,0
        n = int(input())
        if isPrime(n):
            print("NO")
        else:
            flag = False
            for j in range(2,math.ceil(n/2)+1):
                if flag:
                    break
                if n/j == n//j:
                    if not isPrime(n//j):
                        a = j
                        b = n//j
                        flag = True
            flag = False
            for k in range(2,math.ceil(b/2)+1):
                if flag:
                    break
                if b/k == b//k:
                    if not isPrime(b//k):
                        b = b//k
                        c = k
                        flag = True
            if a == 0 or b == 0 or c == 0:
                print("NO")
            else:
                print("YES")
                print(a,b,c)


if __name__ == '__main__':
    main()