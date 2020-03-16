import math
def main():
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        print(1)
    else:
        a = math.ceil(W/2) * math.ceil(H/2)
        b = math.floor(W/2) * math.floor(H/2)
        print(a+b)

if __name__ == '__main__':
    main()