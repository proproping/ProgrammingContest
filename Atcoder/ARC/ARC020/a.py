def main():
    A,B = map(int,input().split())
    if abs(A) > abs(B):
        print("Bug")
    elif abs(A) < abs(B):
        print("Ant")
    else:
        print("Draw")

if __name__ == '__main__':
    main()