import math

def main():
    T = int(input()):
    for i in range(T):
        n,g,b = map(int,input().split())
        high = g
        low = 0
        day = g
        if math.ceil(n/2) <= g:
            print(n)
        else:
            rem = math.ceil(n/2) - g

if __name__ == '__main__':
    main()